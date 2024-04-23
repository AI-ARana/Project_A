# tenants/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenant_list, name='tenant_list'),
    path('add_tenant/', views.add_tenant, name='add_tenant'),
    path('add/', views.add_tenant, name='add_tenant'),
    path('update_tenant/<int:tenant_id>/', views.update_tenant, name='update_tenant'),
    path('delete_tenant/<int:tenant_id>/', views.delete_tenant, name='delete_tenant'),
]
