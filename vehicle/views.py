from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, ListView

from vehicle.forms import VehicleForm
from vehicle.models import Vehicle


class VehicleListView(SuccessMessageMixin, ListView):
    model = Vehicle
    queryset = Vehicle.objects.all()
    template_name = 'vehicles/list.html'
    context_object_name = 'vehicles'


class VehicleCreateView(SuccessMessageMixin,
                        CreateView):
    model = Vehicle
    template_name = 'vehicles/create.html'
    form_class = VehicleForm
    success_message = gettext_lazy('Новый автомобиль успешно добавлен')
    success_url = reverse_lazy('list_vehicles')

    def get_initial(self):
        initial = super().get_initial()
        initial['drivers'] = []
        return initial
