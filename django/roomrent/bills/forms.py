from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['tenant', 'amount', 'bill_type', 'date']  # Adjust fields as per your Bill model
