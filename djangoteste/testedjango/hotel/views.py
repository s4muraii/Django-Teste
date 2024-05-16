from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto
from .forms import nome


def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, "homepage.html", context)


def quartos(request):
    context = {}
    dados_quartos = quarto.objects.all()
    context["dados_quartos"] = dados_quartos
    return render(request, "quartos.html", context)

def nome(request):
    if request.method == "POST":
        form = nome(request.POST)

        if form.is_valid():

            return HttpResponse("<h1>thanks!</h1>")

    else:
        form = nome()

    return render(request, "nome.html", {"form": form})