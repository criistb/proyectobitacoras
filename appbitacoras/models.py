from django.db import models

# Create your models here.

class user(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    id_area = models.CharField(max_length=40)

class bitacora(models.Model):

    id = models.AutoField(primary_key=True)
    numerobit = models.CharField(max_length=40)
    asignedto = models.CharField(max_length=50)
    dateini = models.DateField(auto_now_add=True)
    datefin = models.DateField()
    compañia = models.CharField(max_length=40)


class area(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    proceso = models.CharField(max_length=80)
    servicio = models.CharField(max_length=80)
    ans = models.IntegerField()




