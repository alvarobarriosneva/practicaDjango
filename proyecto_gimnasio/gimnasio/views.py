from django.shortcuts import render
from .models import Socio, Entrenador, Clase


def lista_socios(request):
    socios = Socio.objects.all()
    return render(
        request,
        "gimnasio/socios.html",
        {"socios": socios}
    )


def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(
        request,
        "gimnasio/entrenadores.html",
        {"entrenadores": entrenadores}
    )


def lista_clases(request):
    clases = Clase.objects.select_related("entrenador").all()
    return render(
        request,
        "gimnasio/clases.html",
        {"clases": clases}
    )