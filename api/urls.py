from django.urls import include, path
from api import views


urlpatterns = [
    path('v1/auth/', include('rest_framework.urls')),
    path('v1/vehicles', views.VehicleList.as_view()),
    path('v1/drivers', views.DriverList.as_view()),
    path('v1/brands', views.BrandList.as_view()),
    path('v1/enterprises', views.EnterpriseList.as_view()),

    path('v1/test/vehicles', views.TestVehicleList.as_view()),
    path('v1/test/drivers', views.TestDriverList.as_view()),
]
