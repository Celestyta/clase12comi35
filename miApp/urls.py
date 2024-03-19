from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:nombre>/<str:apellido>/<int:edad>' , views.crear_usuario, name = "Crear usuario")
]