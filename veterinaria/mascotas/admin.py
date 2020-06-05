from django.contrib import admin

# Importamos nuestro modelo
from .models import Mascota

# Registramos la Clase y la visualización en el Administrador
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre','especie','raza']