from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),  # Liste des inventaires
    path('inventory/<int:inventory_id>/', views.weapon_list, name='weapon_list'),  # Armes pour un inventaire
    path('weapon/<int:weapon_id>/', views.skin_list, name='skin_list'),  # Skins pour une arme
    path('inventories/create/', views.create_inventory, name='create_inventory'),
    path('weapons/create/', views.create_weapon, name='create_weapon'),
    path('skins/create/', views.create_skin, name='create_skin'),
]
