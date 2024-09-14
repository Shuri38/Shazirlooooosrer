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
    
    class Meta:
        app_label = 'public'

class Armes(models.Model):
    name = models.CharField(max_length=100)
    weapon_type = models.CharField(max_length=50)
    damage = models.IntegerField()
    inventory = models.ForeignKey('Inventaires', on_delete=models.CASCADE, related_name='weapons',null=True)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'public'

class Inventaires(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventories',null=True)

    def __str__(self):
        return f"Inventaire de {self.user.username}"

    class Meta:
        app_label = 'public'