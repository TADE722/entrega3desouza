from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro



def inicio(request):
    template = loader.get_template("inicio.html")
    segundos = datetime.now().second
    diccionario = {
    "mensaje": "alilililili",
    "segundos": segundos,
    "segundo_par" : segundos%2 == 0,
    "segundo_redondo": segundos%10 == 0,
    "listado_de_numeros" : list(range(25))
    }
    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)




def segunda_vista(request):
    return HttpResponse("<h1>soy la segunda vista</h1>")



def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f"la fecha es: {fecha}")

def saludo(request):
    return HttpResponse("hola")

def bienvenida(request, nombre, apellido):
    return HttpResponse(f"bienvenido {nombre} {apellido}!!!") 

def crear_perro(request, nombre, edad):
    Template = loader.get_template("crear_perro.html")
    perro = Perro(nombre=nombre,edad=edad)
    perro.save()
    diccionario = {
        "perro":perro,
    }
    renderizar_template = Template.render(diccionario)
    return HttpResponse(renderizar_template)

