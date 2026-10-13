from django.urls import path
from . import views

urlpatterns = [
    path("socios/", views.lista_socios, name="lista_socios"),
    path(
        "entrenadores/",
        views.lista_entrenadores,
        name="lista_entrenadores"
    ),
    path("clases/", views.lista_clases, name="lista_clases"),
]