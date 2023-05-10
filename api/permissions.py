from rest_framework.permissions import BasePermission

from vehicle.models import Manager, Driver,Vehicle


class IsManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return len(Manager.objects.filter(user=request.user)) > 0 or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        manager = Manager.objects.filter(user=request.user)[0]
        enterprises = manager.enterprises.all()
        if obj.__class__.__name__ == 'Driver':
            drivers = Driver.objects.filter(enterprise__in=enterprises)
            if obj in drivers:
                return True
        if obj.__class__.__name__ == 'Vehicle':
            vehicles = Vehicle.objects.filter(enterprise__in=enterprises)
            if obj in vehicles:
                return True
        return False
