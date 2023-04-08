from django.contrib import admin

from vehicle.models import Brand, Vehicle


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'number', 'price', 'release_year', 'mileage', 'brand'
    )


admin.site.register(Brand, BrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)
