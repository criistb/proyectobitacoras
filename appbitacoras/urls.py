from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('user', views.user, name="user"),
    path('bitacora', views.bitacora, name="bitacora"),
    path('area', views.area, name="area"),
    path('bitacoraFormulario', views.bitacoraFormulario, name="bitacoraFormulario")
]


