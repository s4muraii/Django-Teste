from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='home'),
    path("quartos/", views.quartos),
    path ('/nome', views.nome, name='nome')
]