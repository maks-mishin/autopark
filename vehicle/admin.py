from django.contrib import admin
from vehicle.models import Vehicle, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'number', 'price', 'release_year',
        'mileage', 'brand'
    )
