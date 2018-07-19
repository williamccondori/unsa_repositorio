from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from repositorio.dtos.response import Response
from repositorio.services.calificador_service import CalificadorService
from repositorio.dtos.calificador_dto import CalificadorDto

import repositorio.helpers.parseador_json as encode


class CalificadorApiController(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CalificadorApiController, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            calificador_service = CalificadorService()
            calificador_dto = CalificadorDto()

            json_data = encode.to_json_object(request.body)
            calificador_dto.from_json(json_data)
            calificador_dto.IpUsuario = self.obtener_ip_cliente(request)

            resultado = calificador_service.cafilicar(calificador_dto)
            return JsonResponse(encode.to_json(
                Response(datos=resultado)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def obtener_ip_cliente(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
