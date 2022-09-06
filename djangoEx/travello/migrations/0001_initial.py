# Generated by Django 4.1.1 on 2022-09-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destination",
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
                ("name", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="pics")),
                ("desc", models.TextField()),
                ("offer", models.BooleanField(default=False)),
            ],
        ),
    ]
