from django import forms


class UserFormulario(forms.Form):
    
    nombre = forms.CharField()
    email = forms.EmailField()
    id_area = forms.CharField()

class BitacoraFormulario(forms.Form):
 
    numerobit = forms.CharField()
    asignedto = forms.CharField()
    dateini = forms.DateField()
    datefin = forms.DateField()
    compañia = forms.CharField()


class AreaFormulario(forms.Form):

    nombre = forms.CharField()
    proceso = forms.CharField()
    servicio = forms.CharField()
    ans = forms.IntegerField()