from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def vista_pagina_inicio(request):
    return HttpResponse("Hola mundo, me llamo Guillermo!")
