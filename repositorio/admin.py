from django.contrib import admin
from .models import Autor
from .models import Documento
from .models import Puntuacion
# Register your models here.

admin.site.register(Autor)
admin.site.register(Documento)