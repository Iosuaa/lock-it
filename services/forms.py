from django import forms
from django.forms import TextInput

from services.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Type service name'}),
            'username': TextInput(attrs={'placeholder': 'Type a username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Type a password'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['name'].requierd = True
        self.fields['username'].requierd = True
        self.fields['password'].requierd = True

    def clean(self):
        name = self.cleaned_data.get('name')
        all_services = Service.objects.all()
        for service in all_services:
            if name == service.name:
                msg = 'This service is already saved in vault!'
                self._errors['name'] = self.error_class([msg])
