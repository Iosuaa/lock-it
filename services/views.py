from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from services.forms import ServiceForm
from services.models import Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'services/service_create.html'
    model = Service
    success_url = reverse_lazy('service_list')
    form_class = ServiceForm


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = 'services/service_list.html'
    model = Service
    context_object_name = 'all_services'


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = ''
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = ''
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('service_list')
