from repositorio.dtos.documento_dto import DocumentoDto
from repositorio.dtos.autor_dto import AutorDto
from repositorio.models import Documento


class BuscadorService(object):

    def buscar(self, expresion):
        documentos_dto = []

        documentos = Documento.objects.filter(titulo__contains=expresion)

        for documento in documentos:
            documentos_dto.append(DocumentoDto(
                id=documento.id,
                titulo=documento.titulo,
                anio=documento.anio,
                resumen=documento.resumen,
                autor=AutorDto(
                    id=documento.autor.id,
                    nombre=documento.autor.nombre,
                    apellido=documento.autor.apellido,
                    nombre_completo='{0} {1}'.format(
                        documento.autor.apellido, documento.autor.nombre),
                    email=documento.autor.email
                )
            ))

        return documentos_dto
