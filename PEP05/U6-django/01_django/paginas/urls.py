#cuando llegue una peticion, lanzamos lo que tebgamos que lanzar

from django.urls import path
from .views import vista_pagina_inicio

urlpatterns = [
    path("", vista_pagina_inicio),
]