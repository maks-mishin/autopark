from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsManagerPermission
from api.serializers import VehicleSerializer, BrandSerializer, \
    EnterpriseSerializer, DriverSerializer
from vehicle.models import Vehicle, Brand, Enterprise, Driver, Manager


@permission_classes((AllowAny,))
class TestVehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


@permission_classes((AllowAny,))
class TestDriverList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(APIView):
    permission_classes = (IsManagerPermission,)
    parser_classes = (JSONParser,)

    def check_permissions(self, request):
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(request, message='Error code: 401', code=401)

    def check_object_permissions(self, request, obj):
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(request, message='Error code: 403', code=403)

    def get(self, request):
        if request.user.is_superuser:
            vehicles = Vehicle.objects.all()
        elif Manager.objects.filter(user=request.user):
            mngr = Manager.objects.filter(user=request.user)[0]
            enterprises = mngr.enterprises.all()
            vehicles = Vehicle.objects.filter(enterprise__in=enterprises)
        else:
            print('Error in server logic, should have failed on "check_permissions" stage.')
            self.permission_denied(request, message='Error code: 401', code=401)

        page = request.GET.get('page', 1)
        paginator = Paginator(vehicles, 20)
        try:
            vehicles = paginator.page(page)
        except PageNotAnInteger:
            vehicles = paginator.page(1)
        except EmptyPage:
            vehicles = paginator.page(paginator.num_pages)
        serialized_vehicles = VehicleSerializer(instance=vehicles, many=True)
        return Response(serialized_vehicles.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if request.user.is_superuser or (Manager.objects.filter(user=request.user) and request.user.is_staff):
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetail(APIView):
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class EnterpriseList(generics.ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class DriverList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
