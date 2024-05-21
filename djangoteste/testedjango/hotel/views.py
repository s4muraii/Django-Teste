from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, cadastro
from .forms import CheckinForm


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


def checkin(request):
    if request.method == "POST":
        form = CheckinForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            user = cadastro(nome=nome, email=email)
            user.save()

            return HttpResponse("Checkin realizado com sucesso!")
    else:
        form = CheckinForm()
    return render(request, "form.html", {"form": form})