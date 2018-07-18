from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

SECRET_TOKEN='repositoriounsa'

class WebhookApiController(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhookApiController, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        respuesta = self.request.GET
        if respuesta['hub.mode'] == 'subscribe':
            if respuesta['hub.verify_token'] == SECRET_TOKEN:
                return HttpResponse(respuesta['hub.challenge'])
            else:
                return HttpResponse('El token es inválido.')
        return HttpResponse('No es un request de tipo subscribe.')

    def post(self, request, *args, **kwargs):  
        cadena_json = request.body
        respuesta = json.loads(cadena_json)
        return HttpResponse('Ok')