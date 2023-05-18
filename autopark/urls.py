from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from vehicle.views import ManagerLoginView, ManagerCreateView, EnterpriseList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicle.urls')),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('managers/login/', ManagerLoginView.as_view(), name='login'),
    path('managers/create/', ManagerCreateView.as_view(), name='create_user'),
    path('enterprises/', EnterpriseList.as_view(), name='list_enterprises'),

]
