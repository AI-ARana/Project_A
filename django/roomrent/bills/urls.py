from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('add/', views.add_bill, name='add_bill'),
    path('update/<int:bill_id>/', views.update_bill, name='update_bill'),
    path('delete/<int:bill_id>/', views.delete_bill, name='delete_bill'),
]
