from repositorio.models import Puntuacion, Cliente

from repositorio.dtos.calificador_dto import CalificadorDto
from repositorio.dtos.tipo_cliente_dto import TipoClienteDto


class CalificadorService(object):

    def cafilicar(self, calificador_dto):
        return True

    def verificar_usuario(self, calificador_dto):
        existe_web = Cliente.objects.filter(
            ip_usuario=calificador_dto.IpUsuario, tipo_cliente_id=TipoClienteDto.WEB).exists()

        existe_bot = Cliente.objects.filter(
            id_usaurio=calificador_dto.IdUsuario, tipo_cliente_id=TipoClienteDto.BOT).exists()
        return existe_web or existe_bot
