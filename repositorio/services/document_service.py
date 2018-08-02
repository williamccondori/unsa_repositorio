from repositorio.dtos.document_dto import DocumentDto

from repositorio.models import Documento

class DocumentService(object):
    def get_by_id(self, id):
        pass

    def save(self, document_dto):
        document = Documento(
            titulo=document_dto.title,
            anio=document_dto.year,
            resumen=document_dto.summary,
            autor_id=document_dto.author_id,
            url=document_dto.document_file
        )
        