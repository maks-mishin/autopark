from django.urls import include, path
from vehicle.views import VehicleCreateView, VehicleListView

urlpatterns = [
    path('create/', VehicleCreateView.as_view(), name='create_vehicle'),
    path('', VehicleListView.as_view(), name='list_vehicles'),
]
