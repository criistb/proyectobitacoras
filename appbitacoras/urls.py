from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('userBit', views.userBit, name="UserBit"),
    path('bitacora', views.bitacora, name="bitacora"),
    path('area', views.area, name="area"),
    path('buscar/', views.buscar),
    path('leerusuariosBit', views.leerUserBit, name = "LeerUsuarioBit"),
    path('eliminarusuarioBit/<user_nombre>/', views.eliminarUserBit, name="EliminarUsuarioBit"),
    path('editarusuarioBit/<user_nombre>/', views.editarUserBit, name="EditarUsuarioBit"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='appbitacoras/logout.html'), name='Logout'),
    path('contacto', views.contacto, name='Contacto'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    #path('bitacoraFormulario', views.bitacoraFormulario, name="bitacoraFormulario")
]


