from django.urls import path
from .views import api_data, inventaires, armes, skins

urlpatterns = [
    path('data/', api_data, name='api_data'),
    path('inventaire/',inventaires, name='inventaires'),
    path('armes/',armes,name='armes'),
    path('skins/',skins, name='skins')
]