# Generated by Django 4.2.7 on 2024-04-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tenant",
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
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("occupation", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("move_in_date", models.DateField()),
                ("rent_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "security_deposit",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]