from django.urls import path
from . import views


app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/<int:id>/', views.inventory_lookup_view, name='inventory-lookup'),
    path('inventory/<int:id>/delete/', views.delete_view, name='inventory-delete'),
    path('inventory/inventory-list', views.inventory_list_view, name='inventory-list')
]
