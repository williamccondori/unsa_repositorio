from django.urls import path
from repositorio.api_controllers.message_api_controller import MessageApiController
from repositorio.api_controllers.buscador_api_controller import BuscadorApiController

API_NAME='api_'

urlpatterns = [
    path('message', MessageApiController.as_view(), name=API_NAME + 'message'),
    path('search', BuscadorApiController.as_view(), name=API_NAME + 'search')
]