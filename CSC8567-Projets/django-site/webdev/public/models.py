# api/models.py
from django.db import models
from django.contrib.auth.models import User

class Skins(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    weapon = models.ForeignKey('Armes', on_delete=models.CASCADE, related_name='skins',null=True)
    image = models.ImageField(upload_to='skins/', null=True)

    def __str__(self):
        return self.name

class Armes(models.Model):
    name = models.CharField(max_length=100)
    weapon_type = models.CharField(max_length=50)
    damage = models.IntegerField()
    inventory = models.ForeignKey('Inventaires', on_delete=models.CASCADE, related_name='weapons',null=True)

    def __str__(self):
        return self.name

class Inventaires(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories',null=True)

    def __str__(self):
        return f"Inventaire de {self.user.username}"
    
class Bungalow(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()  # Nombre total de places
    available_places = models.IntegerField()  # Places disponibles
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.available_places} places disponibles)"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE, related_name='reservations')
    places_reserved = models.IntegerField()

    def __str__(self):
        return f"Réservation de {self.places_reserved} places par {self.user.username} pour {self.bungalow.name}"