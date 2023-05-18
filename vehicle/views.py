from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views import View
from django.views.generic import CreateView, ListView, FormView

from vehicle.forms import VehicleForm, ManagerLoginForm, ManagerCreateForm
from vehicle.models import Vehicle, Enterprise, Manager


class EnterpriseList(View):
    def get(self, request, *args, **kwargs):
        manager_name = ''
        if request.user.is_superuser:
            enterprises = Enterprise.objects.all()
        if Manager.objects.filter(user=request.user):
            manager = Manager.objects.filter(user=request.user)[0]
            enterprises = manager.enterprises.all()
            manager_name = manager.user.first_name + ' ' + manager.user.last_name
        return render(
            request,
            'vehicles/list_enterprises.html',
            {
                'enterprises': enterprises,
                'manager_name': manager_name
            }
        )


class VehicleListView(SuccessMessageMixin, ListView):
    model = Vehicle
    paginate_by = 50
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


class ManagerLoginView(SuccessMessageMixin, LoginView):
    model = Manager
    template_name = 'managers/sign_in.html'
    form_class = ManagerLoginForm
    next_page = reverse_lazy('list_enterprises')
    success_message = gettext_lazy('Вы залогинены')


class ManagerCreateView(CreateView, SuccessMessageMixin, FormView):
    model = Manager
    template_name = 'managers/create.html'
    form_class = ManagerCreateForm
    success_url = reverse_lazy('login')
    success_message = gettext_lazy('Менеджер успешно зарегистрирован')
