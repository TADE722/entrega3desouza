from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def inicio(request):
    archivo = open(r"C:\Users\Tadeo de Souza\Dropbox\Mi PC (DESKTOP-DMHN27A)\Desktop\coder_python\FirstDjango\templates\inicio.html", "r")
    template = Template(archivo.read())
    archivo.close
    contexto = Context()
    renderizar_template = template.render(contexto)

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