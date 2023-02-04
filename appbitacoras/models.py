from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UsuarioBit(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    id_area = models.CharField(max_length=40)

    def __str__(self):

        return f"Nombre: {self.nombre} - Email: {self.email} - Id_area: {self.id_area}"

class Bitacora(models.Model):

    id = models.AutoField(primary_key=True)
    numerobit = models.CharField(max_length=40)
    asignedto = models.CharField(max_length=50)
    dateini = models.DateField(auto_now_add=True)
    datefin = models.DateField()
    compañia = models.CharField(max_length=40)


class Area(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    proceso = models.CharField(max_length=80)
    servicio = models.CharField(max_length=80)
    ans = models.IntegerField()

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"




