from django.urls import path
from MyApp import views

app_name = "MyApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("clientes/", views.clientes, name="clientes"),
    path("producto/", views.producto, name="producto"),
    path("personal/", views.personal, name="personal"),
]
