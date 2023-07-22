from rest_framework import serializers
from vehicle.models import Vehicle, Brand


class VehicleSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Brand.objects.all()
    )

    class Meta:
        model = Vehicle
        fields = '__all__'

    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
