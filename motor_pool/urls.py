from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicle.urls')),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
