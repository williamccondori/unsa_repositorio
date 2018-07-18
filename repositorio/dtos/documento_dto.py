from .autor_dto import AutorDto

class DocumentoDto(object):
    
    def __init__(self, 
        id=0, 
        titulo='', 
        anio=0, 
        resumen=0,
        autor=AutorDto()):
        self.Id = id
        self.Titulo = titulo
        self.Anio = anio
        self.Resumen = resumen
        self.Autor = autor