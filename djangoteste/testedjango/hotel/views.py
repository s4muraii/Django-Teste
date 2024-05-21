from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, Checkin
from .forms import CheckinForm, CadastroForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


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
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.method == "POST":
        form = CheckinForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            sobre_nome = form.cleaned_data["sobrenome"]
            email = form.cleaned_data["email"]
            tipo_quarto = form.cleaned_data["tipo_quarto"]
            data_reserva = form.cleaned_data["data_reserva"]
            checkin = Checkin(
                nome=nome,
                email=email,
                tipo_quarto=tipo_quarto,
                data_reserva=data_reserva,
                sobrenome=sobre_nome,
            )
            checkin.save()

            return HttpResponse("Checkin realizado com sucesso!")
    else:
        form = CheckinForm()
    return render(request, "checkin.html", {"form": form})


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            nome = form.cleaned_data["nome"]
            sobrenome = form.cleaned_data["sobrenome"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha,
                first_name=nome,
                last_name=sobrenome,
            )
            user.save()
            return HttpResponse("Cadastro realizado com sucesso!")
    else:
        form = CadastroForm()
    return render(request, "cadastro.html", {"form": form})


def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            senha = form.cleaned_data["senha"]
            user = authenticate(username=username, password=senha)
            if user is not None:
                login(request, user)
                return HttpResponse("Login realizado com sucesso!")
            else:
                return HttpResponse("Login ou senha inválidos!")

    else:
        form = LoginForm(request.POST)
    return render(request, "login.html", {"form": form})


def reserva(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    else:
        return HttpResponse("h1>Reserva De Quarto</h1>")