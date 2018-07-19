from django.contrib import admin
from .models import Autor
from .models import Documento
from .models import Puntuacion
from .models import TipoCliente
from .models import Cliente
# Register your models here.

admin.site.register(Autor)
admin.site.register(Documento)
admin.site.register(TipoCliente)
admin.site.register(Cliente)