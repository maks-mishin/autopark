from rest_framework import serializers
from vehicle.models import Brand, Vehicle, Driver, Enterprise


class VehicleSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(many=False, queryset=Brand.objects.all())

    class Meta:
        model = Vehicle
        fields = '__all__'

    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



