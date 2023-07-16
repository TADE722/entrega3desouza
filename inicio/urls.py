from django.urls import path
from inicio import views # IMPORTO DESDE views.py

app_name = "inicio" #por si llegamos a crear dos urls con el mismo nombre pero con diferente app usamos esta funcion para diferenciarlas

urlpatterns = [
    path("",views.inicio, name= "inicio"),
    path("prueba", views.prueba, name= "prueba"), 
    path("segunda-vista/",views.segunda_vista, name="segunda_vista"),
    path("fecha-actual/",views.fecha_actual, name="fecha_actual"),
    path("saludo/",views.saludo, name="saludo"),
    path("bienvenida/<str:nombre>/<str:apellido>/",views.bienvenida, name="bienvenida"),
    
    #path("crear-perro/<str:nombre>/<int:edad>/",views.crear_perro, name="crear_perro"),
    #VISTAS COMUNES
    #path("perro/",views.listar_perro, name="listar_perro"),
    #path("perro/crear/",views.crear_perro, name="crear_perro"),
    #path("perro/modificar/<int:perro_id>/",views.modificar_perro, name="modificar_perro"),
    #path("perro/eliminar/<int:perro_id>/",views.eliminar_perro, name="eliminar_perro"),


    #CBV
    path("perro/crear/",views.CrearPerro.as_view(), name="crear_perro"),
    path("perros/",views.ListarPerros.as_view(), name="listar_perros"),
    path("perro/modificar/<int:pk>/",views.ModificarPerro.as_view(), name="modificar_perro"),
    path("perro/eliminar/<int:pk>/",views.EliminarPerro.as_view(), name="eliminar_perro"),
    path("perro/<int:pk>/",views.MostrarPerro.as_view(), name="mostrar_perro"),


]
