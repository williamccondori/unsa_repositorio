from django.urls import path
from repositorio.api_controllers.message_api_controller import MessageApiController

API_NAME='api_'

urlpatterns = [
    path('message', MessageApiController.as_view(), name=API_NAME + 'message')
]