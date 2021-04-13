from django.urls import path

from services.views import ServiceCreateView, ServiceListView, ServiceUpdateView, ServiceDeleteView

app_name = 'services'

urlpatterns = [
    path('service-create/', ServiceCreateView.as_view(), name='service_create'),
    path('service-list/', ServiceListView.as_view(), name='service_list'),
    path('service-update/<int:pk>', ServiceUpdateView.as_view(), name='service_update'),
    path('service-delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),

]
