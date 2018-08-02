from django.views.generic import View
from django.http import JsonResponse
from repositorio.dtos.response import Response
from repositorio.services.document_service import DocumentService

import repositorio.helpers.parseador_json as encode

class DetailApiController(View):
    def get(self, request, *args, **kwargs):
        try:
            document_service = DocumentService()
            id = request.GET.get('id', '')
            resultado = document_service.get_by_id(id)
            return JsonResponse(encode.to_json(
                Response(datos=resultado)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        return 'Cambios menores'
