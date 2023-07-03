from django.urls import path
from inicio import views # IMPORTO DESDE views.py

urlpatterns = [
 path("", views.inicio), # CREAMOS LA VISTA DE INICIO CON AYUDA DEL ARCHIVO views.py
    path("segunda-vista/",views.segunda_vista),
    path("fecha-actual/",views.fecha_actual),
    path("saludo/",views.saludo),
    path("bienvenida/<str:nombre>/<str:apellido>/",views.bienvenida),
    path("crear-perro/<str:nombre>/<int:edad>/",views.crear_perro),
]