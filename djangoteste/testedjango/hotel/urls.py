from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", views.homepage),
    path("quartos/", views.quartos),
    path("checkin/", views.checkin),
    path("cadastro/", views.cadastro),
    path("login/", views.Login),
    path("reserva/", views.reserva),
]