from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from repositorio.dtos.response import Response
from repositorio.services.buscador_service import BuscadorService

import repositorio.helpers.parseador_json as encode


class BuscadorApiController(View):
    def get(self, request, *args, **kwargs):
        try:
            buscador_service = BuscadorService()
            expresion = request.GET.get('expression', '')
            resultado = buscador_service.buscar(expresion)
            return JsonResponse(encode.to_json(
                Response(datos=resultado)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        return 'No se encuentra'
