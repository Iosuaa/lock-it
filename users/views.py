from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreateUserForm


class UserCreateView(CreateView):
    template_name = 'users/user_create.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = CreateUserForm
