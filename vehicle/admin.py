from django.contrib import admin

from vehicle.models import Brand, Vehicle, Enterprise, Driver


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'number', 'price', 'release_year', 'mileage', 'brand',
        'enterprise'
    )
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'salary', 'enterprise', 'vehicle', 'is_active')
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'country')
    actions_on_bottom = True
    actions_on_top = False
