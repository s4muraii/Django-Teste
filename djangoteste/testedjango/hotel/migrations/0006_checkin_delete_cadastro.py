# Generated by Django 5.0.5 on 2024-05-21 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('tipo_quarto', models.CharField(choices=[('SOLTEIRO', 'Solteiro'), ('CASAL', 'Casal'), ('CONFORT', 'Confort'), ('LUXO', 'Luxo')], max_length=15)),
                ('data_reserva', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='cadastro',
        ),
    ]
