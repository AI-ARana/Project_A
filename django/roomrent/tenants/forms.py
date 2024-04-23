# tenants/forms.py


from django import forms
from tenants.models import Tenant

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'room_number','email', 'phone_number', 'aadhar_number','address', 'occupation','company_address', 'date_of_birth', 'move_in_date', 'rent_amount', 'security_deposit', 'is_active']

"""# tenants/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import models

class YourModelForm(forms.ModelForm):
    class Meta:
        model = models
        fields = ['name', 'email', 'phone_number','aadhar_number', 'address', 'occupation','company_address', 'date_of_birth', 'move_in_date', 'rent_amount', 'security_deposit', 'is_active']
        labels = {
            'name': 'Name',
            'phone_number': 'Phone Number (*Without Country Code)',
            'aadhar_number': 'Aadhar Number',
            'address':'Address',
            'occupation': 'Occupation',
            'company_address': 'Company Address',
            'date_of_birth': 'DOB',
            'move_in_date': 'Start Date as Tenant',
            'rent_amount': 'Rent (* in Rupees)',
            'security_deposit': 'Security Amount (* minimum Rs 1000/-)',
            'is_active': 'Status (Active/Not Active)'

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        return phone_number
        """