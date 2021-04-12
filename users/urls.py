from django.urls import path

from users.views import UserCreateView

urlpatterns = [
    path('user-create/', UserCreateView.as_view(), name='create-user')
]