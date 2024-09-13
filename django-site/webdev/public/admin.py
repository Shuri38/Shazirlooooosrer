# api/admin.py
from django.contrib import admin
from .models import Skins, Armes, Inventaires

@admin.register(Skins)
class SkinsAdmin(admin.ModelAdmin):
    list_display = ['name', 'rarity', 'weapon','image']

@admin.register(Armes)
class ArmesAdmin(admin.ModelAdmin):
    list_display = ['name', 'weapon_type', 'damage', 'inventory']

@admin.register(Inventaires)
class InventairesAdmin(admin.ModelAdmin):
    list_display = ['user']
