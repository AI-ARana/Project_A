from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill
from .forms import BillForm
from .forms import TenantForm

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills/bill_list.html', {'bills': bills})

def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm()
    return render(request, 'bills/add_bill.html', {'form': form})

def update_bill(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'bills/update_bill.html', {'form': form})

def delete_bill(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bills/delete_bill.html', {'bill': bill})
