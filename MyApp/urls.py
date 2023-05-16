from django.urls import path
from MyApp import views
from MyApp.views import (
    listar_clientes,
    crear_cliente,
    buscar_clientes,
    eliminar_cliente,
    editar_cliente,
    PersonalListView,
    PersonalCreateView,
    PersonalDetailView,
    PersonalDeleteView,
    PersonalFormulario,
    PersonalUpdateView,
)

app_name = "MyApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("clientes/", views.clientes, name="clientes"),
    path("producto/", views.producto, name="producto"),
    path("personal/", views.personal, name="personal"),
    path("lista_clientes/", views.crear_cliente, name="crear_cliente"),
    path("lista_personal/", views.PersonalListView.as_view(), name="crear_personal"),
    path("ver_personal/", views.PersonalListView.as_view(), name="ver_personal"),
    path("editar_personal/", PersonalUpdateView.as_view(), name="editar_personal"),
    path("personal/<int:pk>/", PersonalDetailView.as_view(), name="ver_personal"),
    path("crear-personal/", PersonalCreateView.as_view(), name="crear_personal"),
    path(
        "eliminar-personal/<int:pk>/",
        PersonalDeleteView.as_view(),
        name="eliminar_personal",
    ),
]
