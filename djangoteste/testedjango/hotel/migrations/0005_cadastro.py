# Generated by Django 5.0.5 on 2024-05-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_remove_hotel_descricao_hotel_desc_quarto_foto_quarto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
