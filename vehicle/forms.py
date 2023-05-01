from django.forms import ModelForm

from vehicle.models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
