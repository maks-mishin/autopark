from django.urls import include, path
from vehicle import views


urlpatterns = [
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/vehicles', views.VehicleList.as_view()),
    path('api/v1/drivers', views.DriverList.as_view()),
    path('api/v1/brands', views.BrandList.as_view()),
    path('api/v1/enterprises', views.EnterpriseList.as_view()),
]
