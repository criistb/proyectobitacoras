from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appbitacoras.models import *

# Create your views here.

def inicio(request):

      return render(request, "appbitacoras/inicio.html")

def user(request):

      return render(request, "appbitacoras/user.html")

def bitacora(request):

      return render(request, "appbitacoras/bitacora.html")


def area(request):

      return render(request, "appbitacoras/area.html")

from appbitacoras.forms import *

def bitacoraFormulario(request):
      if request.method == "POST":
            
            miFormulario = BitacoraFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  bitacora = bitacora(id=informacion["id"], numerobit=informacion["numerobit"], asignedto=informacion["asignedto"], dateini=informacion["dateini"], datefin=informacion["datefin"], compañia=informacion["compañia"])
                  bitacora.save()
                  return render(request, "appbitacora/inicio.html")
            
      else:
            miFormulario = BitacoraFormulario()

      return render(request, "appbitacora/bitacoraFormulario.html", {"miFormulario": miFormulario})

