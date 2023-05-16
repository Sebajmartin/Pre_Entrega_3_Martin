from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views.generic import TemplateView
from MyApp.models import Producto
from MyApp.models import Personal
from MyApp.models import Cliente
from MyApp.forms import ClienteFormulario
from MyApp.forms import PersonalFormulario
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


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
    contexto = {}
    http_response = render(
        request=request,
        template_name="clientes.html",
        context=contexto,
    )
    return http_response


def producto(request):
    contexto = {"producto": Producto.objects.all()}
    http_response = render(
        request=request,
        template_name="producto.html",
        context=contexto,
    )
    return http_response


from django.shortcuts import render


def personal(request):
    contexto = {"producto": Personal.objects.all()}
    http_response = render(
        request=request,
        template_name="personal.html",
        context=contexto,
    )
    return http_response


from django.urls import reverse_lazy
from django.shortcuts import render, redirect


def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            # Redirecciono al usuario a la lista de cursos
            return redirect(reverse_lazy("lista_clientes"))
    else:  # GET
        formulario = ClienteFormulario()
    return render(
        request=request,
        template_name="lista_clientes.html",
        context={"formulario": formulario},
    )


def buscar_clientes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        clientes = Cliente.objects.filter(nombre__contains=busqueda)
        contexto = {
            "clientes": clientes,
        }
        http_response = render(
            request=request,
            template_name="lista_clientes.html",
            context=contexto,
        )
        return http_response


def listar_clientes(request):
    contexto = {
        "clientes": Cliente.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="lista_clientes.html",
        context=contexto,
    )
    return http_response


def eliminar_cliente(request, id):
    curso = Cliente.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse("lista_clientes")
        return redirect(url_exitosa)


def editar_cliente(request, id):
    curso = Cliente.objects.get(id=id)
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Cliente.nombre = data["nombre"]
            Cliente.apellido = data["apellido"]
            Cliente.email = data["email"]
            Cliente.telefono = data["telefono"]
            Cliente.direccion = data["direccion"]
            Cliente.dni = data["dni"]
            Cliente.save()

            url_exitosa = reverse("lista_cliente")
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            "nombre": Cliente.nombre,
            "apellido": Cliente.apellido,
            "email": Cliente.email,
            "telefono": Cliente.telefono,
            "direccion": Cliente.direccion,
            "dni": Cliente.dni,
        }
        formulario = ClienteFormulario(initial=inicial)
    return render(
        request=request,
        template_name="MyApp/formulario_cliente.html",
        context={"formulario": formulario},
    )


# Vistas de Estudiantes
class PersonalListView(ListView):
    model = Personal
    template_name = "MyApp/lista_estudiantes.html"


class PersonalCreateView(CreateView):
    model = Personal
    fields = ("apellido", "nombre", "telefono", "dni", "email", "sector")
    success_url = reverse_lazy("lista_personal")


class PersonalDetailView(DetailView):
    model = Personal
    success_url = reverse_lazy("lista_personal")


class PersonalUpdateView(UpdateView):
    model = Personal
    fields = ("apellido", "nombre", "telefono", "dni", "email", "sector")
    success_url = reverse_lazy("lista_personal")


class PersonalDeleteView(DeleteView):
    model = Personal
    success_url = reverse_lazy("lista_personal")


class ProductoCreateView(CreateView):
    model = Producto
    fields = ("nombre", "descripcion", "precio", "stock", "imagen", "categoria")
    success_url = reverse_lazy("lista_productos")
    template_name = "MyApp/producto.html"
