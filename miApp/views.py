from django.shortcuts import render
from .models import Usuario
from django.template import Template, Context

def crear_usuario(request, nombre, apellido, edad):
    nuevo_usuario = Usuario.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad
    )
    return render(request, 'nuevo_usuario.html', {'nuevo_usuario' : nuevo_usuario})