from django.shortcuts import render, redirect, get_object_or_404
from .forms import TenantForm
from tenants.models import Tenant

def tenant_list(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants': tenants,
    }
    return render(request, 'tenants/tenant_list.html', context)
   # return render(request, 'tenants/tenant_list.html', {'tenants': tenants})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'tenants/add_tenant.html', {'form': form})

def update_tenant(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/update_tenant.html', {'form': form})

def delete_tenant(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    if request.method == 'POST':
        tenant.delete()
        return redirect('tenant_list')
    return render(request, 'tenants/delete_tenant.html', {'tenant': tenant})

# Create your views here.
