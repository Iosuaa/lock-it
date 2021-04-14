from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from services.forms import ServiceForm, ServiceUpdateForm
from services.models import Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'services/service_create.html'
    model = Service
    success_url = reverse_lazy('services:service_list')
    form_class = ServiceForm

    def form_valid(self, form):
        print(form)
        name = form.cleaned_data['name']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        service = Service.objects.create(user=self.request.user, name=name, username=username, password=password)
        return redirect(self.success_url)


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = 'services/service_list.html'
    model = Service
    context_object_name = 'all_services'

    def get_context_data(self, *, object_list=None, **kwargs):
        services = Service.objects.filter(user=self.request.user)
        return {'all_services': services}


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'services/service_update.html'
    model = Service
    # fields = '__all__'
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('services:service_list')


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'services/service_delete.html'
    model = Service
    fields = '__all__'
    success_url = reverse_lazy('services:service_list')
