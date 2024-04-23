# Generated by Django 4.2.11 on 2024-04-22 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tenant",
            name="phone_number",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.MinLengthValidator(10),
                    django.core.validators.MaxLengthValidator(10),
                ],
            ),
        ),
    ]
