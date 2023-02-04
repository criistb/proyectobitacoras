from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from appbitacoras.models import *
from appbitacoras.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.

#def inicio(request):

      #return render(request, "appbitacoras/inicio.html")

#def user(request):

      #return render(request, "appbitacoras/user.html")

#def bitacora(request):

      #return render(request, "appbitacoras/bitacora.html")


#def area(request):

      #return render(request, "appbitacoras/area.html")

def home(request):
      return render(request,"appbitacoras/home.html")

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


def userBit(request):
      if request.method == "POST":
            
            miFormulario = UserFormularioBit(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  user = UsuarioBit(nombre=informacion["nombre"], email=informacion["email"], id_area=informacion["id_area"])
                  user.save()
                  return render(request, "appbitacoras/inicio.html")
            
      else:
            miFormulario = UserFormularioBit()

      return render(request, "appbitacoras/userBit.html", {"miFormulario": miFormulario})

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

def leerUserBit(request):

      user = UsuarioBit.objects.all() #trae todos los usuarios

      contexto= {"UsersBit":user} 

      return render(request, "appbitacoras/leerUsuariosBit.html",contexto)



def eliminarUserBit(request, user_nombre):
      user = UsuarioBit.objects.get(nombre=user_nombre)
      user.delete()
      # vuelvo al menú
      user = UsuarioBit.objects.all()  # trae todos los usuarios
      contexto = {"Users": user}
      return render(request, "appbitacoras/inicio.html", contexto)
      
      

def editarUserBit(request, user_nombre):
    # Recibe el nombre del usuario que vamos a modificar
    user = UsuarioBit.objects.get(nombre=user_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = UserFormularioBit(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            user.nombre = informacion['nombre']
            user.email = informacion['email']
            user.id_area = informacion['id_area']

            user.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "appbitacoras/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = UserFormularioBit(initial={'nombre': user.nombre,
                                                   'email': user.email, 'id_area': user.id_area})

    # Voy al html que me permite editar
    return render(request, "appbitacoras/editarUsuarioBit.html", {"miFormulario": miFormulario, "usuario_nombre": user_nombre})




def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "appbitacoras/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "appbitacoras/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "appbitacoras/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "appbitacoras/login.html", {"form": form})



def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
            
                  return render(request,"appbitacoras/home.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"appbitacoras/registro.html" ,  {"form":form})


@login_required(login_url='/appbitacoras/login')
def inicio(request):

      #avatares = Avatar.objects.filter(user=request.user.id)

      return render(request, "appbitacoras/inicio.html")#,{"URL": avatares[0].imagen.url})

def contacto(request):

    return render(request, "appbitacoras/contacto.html")


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "appbitacoras/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "appbitacoras/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
