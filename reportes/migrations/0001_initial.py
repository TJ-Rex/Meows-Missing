# Generated by Django 5.1.3 on 2024-11-16 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Nombre", models.CharField(max_length=300)),
                ("Descripcion", models.TextField(max_length=5000)),
                ("Imagen", models.ImageField(upload_to="reportes/images")),
                ("Fecha", models.DateField(verbose_name=datetime.date.today)),
                ("Estado", models.CharField(max_length=300)),
            ],
        ),
    ]