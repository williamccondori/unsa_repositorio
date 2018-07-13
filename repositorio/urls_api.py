from django.urls import path
from repositorio.api_controllers.webhook_api_controller import WebhookApiController

API_NAME='api_'

urlpatterns = [
    path('webhook', WebhookApiController.as_view(), name=API_NAME + 'webhook')
]