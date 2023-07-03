from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro

def prueba(request):
    segundos = datetime.now().second
    diccionario = {
    "mensaje": "alilililili",
    "segundos": segundos,
    "segundo_par" : segundos%2 == 0,
    "segundo_redondo": segundos%10 == 0,
    "listado_de_numeros" : list(range(25))
    }
    return render(request,"inicio/prueba.html",diccionario)


def segunda_vista(request):
    return HttpResponse("<h1>soy la segunda vista</h1>")

def inicio(request):
    return render(request,"inicio/inicio.html")

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f"la fecha es: {fecha}")

def saludo(request):
    return HttpResponse("hola")

def bienvenida(request, nombre, apellido):
    return HttpResponse(f"bienvenido {nombre} {apellido}!!!") 

def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre,edad=edad)
    perro.save()
    diccionario = {
        "perro":perro,
    }
    return render(request,"inicio/crear_perro.html",diccionario)
