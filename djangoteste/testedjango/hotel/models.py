from django.db import models
import datetime 
# Create your models here.

tipos_quartos = (
    ("SOLTEIRO", "solteiro"),
    ("CASAL", "casal"),
    ("CONFORT", "confort"),
    ("LUXO", "luxo")
)

class hotel (models.Model):
    titulo = models.CharField (max_length=50)
    descricao = models.TextField (max_length=200)

class quarto (models.Model):
    tipo = models.CharField (max_length=15, choices=tipos_quartos)
    disponibilidade = models.IntegerField (max_length=9999)
    valor = models.FloatField (max_length=9999)
    descricao = models.TextField (max_length=300)
    data_reserva = models.DateTimeField (default = datetime.datetime.now)