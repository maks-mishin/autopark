from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from api.serializers import VehicleSerializer, BrandSerializer
from vehicle.models import Vehicle, Brand


class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
