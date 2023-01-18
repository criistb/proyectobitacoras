from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appbitacoras.models import *
from appbitacoras.forms import *

# Create your views here.

def inicio(request):

      return render(request, "appbitacoras/inicio.html")

#def user(request):

      #return render(request, "appbitacoras/user.html")

#def bitacora(request):

      #return render(request, "appbitacoras/bitacora.html")


#def area(request):

      #return render(request, "appbitacoras/area.html")

def buscar(request):

      if  request.GET["numerobit"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            
            numerobit = request.GET['numerobit'] 
            asignedto  = Bitacora.objects.filter(numerobit__icontains=numerobit)

            return render(request, "appbitacoras/inicio.html", {"numerobit":numerobit, "asignedto":asignedto})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

from appbitacoras.forms import *


def bitacora(request):
      if request.method == "POST":
            
            miFormulario = BitacoraFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  bitacora = Bitacora(numerobit=informacion["numerobit"], asignedto=informacion["asignedto"], dateini=informacion["dateini"], datefin=informacion["datefin"], compañia=informacion["compañia"])
                  bitacora.save()
                  return render(request, "appbitacoras/inicio.html")
            
      else:
            miFormulario = BitacoraFormulario()

      return render(request, "appbitacoras/bitacora.html", {"miFormulario": miFormulario})


def user(request):
      if request.method == "POST":
            
            miFormulario = UserFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  user = User(nombre=informacion["nombre"], email=informacion["email"], id_area=informacion["id_area"])
                  user.save()
                  return render(request, "appbitacoras/inicio.html")
            
      else:
            miFormulario = UserFormulario()

      return render(request, "appbitacoras/user.html", {"miFormulario": miFormulario})

def area(request):
      if request.method == "POST":
            
            miFormulario = AreaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  user = Area(nombre=informacion["nombre"], proceso=informacion["proceso"], servicio=informacion["servicio"], ans=informacion["ans"])
                  user.save()
                  return render(request, "appbitacoras/inicio.html")
            
      else:
            miFormulario = AreaFormulario()

      return render(request, "appbitacoras/area.html", {"miFormulario": miFormulario})


