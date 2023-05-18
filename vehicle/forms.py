from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from vehicle.models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class ManagerLoginForm(AuthenticationForm):
    username = User.username
    password = User.password
    fields = ['username', 'password1']


class ManagerCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2'
                  ]
