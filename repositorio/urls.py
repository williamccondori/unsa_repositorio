# Se agrega archivo de rutas para la aplicacion repositorio.

from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('repositorio.urls_api')),
    path('', views.dashboard, name='dashboard'),
]