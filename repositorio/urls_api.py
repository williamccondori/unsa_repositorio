from django.urls import path
<<<<<<< HEAD
from repositorio.api_controllers.message_api_controller import MessageApiController
from repositorio.api_controllers.buscador_api_controller import BuscadorApiController
=======
from repositorio.api_controllers.webhook_api_controller import WebhookApiController
>>>>>>> 14cffe540bab930b2caa19348e8cea4a5b5af04c

API_NAME='api_'

urlpatterns = [
<<<<<<< HEAD
    path('message', MessageApiController.as_view(), name=API_NAME + 'message'),
    path('search', BuscadorApiController.as_view(), name=API_NAME + 'search')
=======
    path('webhook', WebhookApiController.as_view(), name=API_NAME + 'webhook')
>>>>>>> 14cffe540bab930b2caa19348e8cea4a5b5af04c
]