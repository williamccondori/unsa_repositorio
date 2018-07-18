from django.urls import path

from repositorio.api_controllers.webhook_api_controller import WebhookApiController
from repositorio.api_controllers.buscador_api_controller import BuscadorApiController
from repositorio.api_controllers.calificador_api_controller import CalificadorApiController

API_NAME='api_'

urlpatterns = [
    path('webhook', WebhookApiController.as_view(), name=API_NAME + 'webhook'),
    path('search', BuscadorApiController.as_view(), name=API_NAME + 'search'),
    path('rate', CalificadorApiController.as_view(), name=API_NAME + 'rate')
]