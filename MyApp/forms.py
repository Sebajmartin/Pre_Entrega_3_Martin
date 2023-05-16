from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=200)
    apellido = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True)
    direccion = forms.CharField(required=True, max_length=200)
    dni = forms.IntegerField(required=True)


class PersonalFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=200)
    apellido = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True, max_length=200)
    direccion = forms.CharField(required=True, max_length=200)
    dni = forms.IntegerField(required=True)
