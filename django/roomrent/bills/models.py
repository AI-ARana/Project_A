from django.db import models
from tenants.models import Tenant

class Bill(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill_type = models.CharField(max_length=20)  # Electricity or Water
    # Add other fields like date, status, etc.

    def __str__(self):
        return f"{self.tenant.name} - {self.bill_type}"
