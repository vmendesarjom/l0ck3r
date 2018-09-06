from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as locker

app_name = 'locker'

urlpatterns = [
    # Projectors
    path('projetores/', locker.ProjectorView.as_view(), name='projector-list'),
    path('projetores/novo/', locker.ProjectorCreateView.as_view(), name='projector-create'),
    path('projetores/<uuid:pk>/editar/', locker.ProjectorEditView.as_view(), name='projector-edit'),

    # Reserve
    path('reserva/novo/', locker.ReserveCreateView.as_view(), name='reserve-create'),
    path('reservas/', locker.ReserveView.as_view(), name='reserve-list'),
    path('reserva/<uuid:pk>', locker.ReserveDeleteView.as_view(), name='reserve-delete'),
    path('reserva/<uuid:pk>', locker.ReserveDetailView.as_view(), name='reserve-detail'),

]