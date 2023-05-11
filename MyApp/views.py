from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views.generic import TemplateView


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html


def saludar_con_html(request):
    contexto = {"usuario": "Pedro"}
    http_responde = render(
        request=request,
        template_name="MyApp/templates/index.html",
        context=contexto,
    )
    return http_responde


def index(request):
    http_response = render(
        request=request,
        template_name="index.html",
    )
    return http_response


def clientes(request):
    contexto = { 
        "clientes": Clientes.objects.all()
    http_response = render(
        request=request,
        template_name="clientes.html",
        context=contexto,
    )


def producto(request):
    contexto = {
        "productos": Productos.objects.all()
    }
    http_response = render(
        request=request,
        template_name="producto.html",
        context=contexto,
    )
    http_response


from django.shortcuts import render


def personal(request):
    contexto = {}
    return render(request, "MyApp/templates/personal.html", contexto)
