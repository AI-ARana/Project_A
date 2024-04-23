# tenants/models.py

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    aadhar_number = models.CharField(max_length=16, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    company_address = models.TextField()
    date_of_birth = models.DateField()
    move_in_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

