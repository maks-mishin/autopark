from django.contrib import admin

from vehicle.models import Brand, Vehicle, Enterprise, Driver, Manager


def get_manager_enterprises(request):
    if Manager.objects.filter(user=request.user):
        manager = Manager.objects.get(user=request.user)
        return manager.enterprises.all()


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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        enterprises = get_manager_enterprises(request)
        if enterprises:
            return qs.filter(enterprise__in=enterprises)
        return qs


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'salary', 'enterprise', 'vehicle', 'is_active')
    actions_on_bottom = True
    actions_on_top = False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        enterprises = get_manager_enterprises(request)
        if enterprises:
            return qs.filter(enterprise__in=enterprises)
        return qs


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'country')
    actions_on_bottom = True
    actions_on_top = False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        enterprises = get_manager_enterprises(request)
        if enterprises:
            return qs.filter(id__in=enterprises)
        return qs


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'list_enterprises')
    actions_on_bottom = True
    actions_on_top = False
