# Generated by Django 5.0.5 on 2024-05-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='disponibilidade',
            field=models.IntegerField(max_length=9999),
        ),
    ]