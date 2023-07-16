from django.db import models

# Create your models here.
class Perro(models.Model): #tratar de poner como nombre algo en singular
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"perro: {self.nombre} - edad:{self.edad}"
    