from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad']
    search_fields=['nombre']

admin.site.register(Usuario, UsuarioAdmin)