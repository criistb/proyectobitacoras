from django.contrib import admin
from .models import * #importamos el archivo models# Register your models here.
#registramos los modelos
admin.site.register(Area)
admin.site.register(UsuarioBit)
admin.site.register(Bitacora)
admin.site.register(Avatar)

