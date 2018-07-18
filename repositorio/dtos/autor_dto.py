class AutorDto(object):
    def __init__(self, 
        id=0, 
        nombre='', 
        apellido='', 
        nombre_completo='',
        email=''):
        self.Id = id
        self.Nombre = nombre
        self.Apellido = apellido
        self.NombreCompleto = nombre_completo
        self.Email = email