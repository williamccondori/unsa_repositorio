class CalificadorDto(object):
    def __init__(self,
                 id=0,
                 id_documento=0,
                 valoracion=0,
                 ip_usuario=''):
        self.Id = id,
        self.IdDocumento = id_documento
        self.Valoracion = valoracion
        self.IpUsuario = ip_usuario

    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.IdDocumento = json_data["IdDocumento"]
        self.Valoracion = json_data["Valoracion"]
        self.IpUsuario = json_data["IpUsuario"]
