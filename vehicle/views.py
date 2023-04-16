from rest_framework import generics
from vehicle.serializers import VehicleSerializer, BrandSerializer, \
    EnterpriseSerializer, DriverSerializer
from vehicle.models import Vehicle, Brand, Enterprise, Driver


class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class EnterpriseList(generics.ListAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class DriverList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
