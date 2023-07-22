from django.urls import include, path
from api import views


urlpatterns = [
    path('v1/auth/', include('rest_framework.urls')),
    path('v1/vehicles/', views.VehicleList.as_view()),
    path('v1/brands/', views.BrandList.as_view())
]
