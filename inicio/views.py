from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro
from inicio.form import CrearPerroFormulario, BuscarPerroFormulario, ModificarPerroFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
"""v1 crear perro
def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre,edad=edad)
    perro.save()
    diccionario = {
        "perro":perro,
    }
    return render(request,"inicio/crear_perro.html",diccionario)
"""
"""
#v2 crear perro
def crear_perro(request):

    if request.method == "POST":
        formulario = CrearPerroFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro = Perro(nombre=info["nombre"],edad=info["edad"])
            perro.save()
            return redirect("inicio:listar_perro")
        else:
            return render(request,"inicio/crear_perro.html",{"formulario": formulario})

    formulario = CrearPerroFormulario()
    return render(request,"inicio/crear_perro.html",{"formulario": formulario})



def listar_perro(request):
    request.GET
    formulario = BuscarPerroFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data["nombre"]
        listado_de_perro  = Perro.objects.filter(nombre__icontains = nombre_a_buscar)    

    formulario = BuscarPerroFormulario()
    return render(request,"inicio/listar_perro.html",{"formulario": formulario, "perros" : listado_de_perro})

def eliminar_perro(request, perro_id):
    perro = Perro.objects.get(id=perro_id)
    perro.delete()
    return redirect("inicio:listar_perro")

def modificar_perro(request, perro_id):
    perro_a_modificar = Perro.objects.get(id=perro_id)

    if request.method == "POST":
        formulario = ModificarPerroFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro_a_modificar.nombre = info["nombre"]
            perro_a_modificar.edad = info["edad"]
            perro_a_modificar.save()
            return redirect("inicio:listar_perro")
        else:
            return render(request,"inicio/modificar_perro.html",{"formulario":formulario})

    formulario = ModificarPerroFormulario(initial={"nombre":perro_a_modificar.nombre, "edad":perro_a_modificar.edad})
    return render(request,"inicio/modificar_perro.html",{"formulario":formulario})
   
""" 
class CrearPerro(CreateView):
    model = Perro
    template_name = "inicio/CBV/crear_perro_CBV.html"
    fields =["nombre","edad","descripcion"]
    success_url = reverse_lazy("inicio:listar_perros")

class ListarPerros(ListView):
    model = Perro
    template_name = "inicio/CBV/listar_perros_CBV.html"
    context_object_name = "perros"

class  ModificarPerro(UpdateView):
    model =  Perro
    template_name = "inicio/CBV/modificar_perro_CBV.html"
    fields =["nombre","edad","descripcion"]
    success_url = reverse_lazy("inicio:listar_perros")

class EliminarPerro(DeleteView):
    model = Perro
    template_name = "inicio/CBV/eliminar_perro_CBV.html"
    success_url = reverse_lazy("inicio:listar_perros")

class MostrarPerro(DetailView):
    model = Perro
    template_name ="inicio/CBV/mostrar_perro_CBV.html"


