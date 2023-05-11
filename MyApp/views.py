from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


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


from django.shortcuts import render


from django.conf import settings


def index(request):
    return render(request, "index.html")


def clientes(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="Web/MyApp/templates/clientes.html",
        context=contexto,
    )


def producto(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="Web/MyApp/templates/producto.html",
        context=contexto,
    )


from django.shortcuts import render


def personal(request):
    contexto = {}
    return render(request, "MyApp/templates/personal.html", contexto)
