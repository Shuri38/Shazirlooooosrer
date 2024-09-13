from django.shortcuts import render
from .models import *

# Create your views here.
from django.http import JsonResponse

def api_data(request):
    # Exemple de données JSON
    data = {
        "nom": "Jean Dupont",
        "âge": 30,
        "profession": "Développeur",
        "compétences": ["Python", "Django", "JavaScript"],
        "inventaires": str(Inventaires.objects.all()),
    }
    return JsonResponse(data)

def inventaires(request):
    data = {

         "inventaires": str(Inventaires.objects.all()),

    }
    return JsonResponse(data)

def armes(request):
    data = {

        "armes": str(Armes.objects.all()),

    }
    return JsonResponse(data)

def skins(request):
    data = {
        "skins": str(Skins.objects.all())
    }
    return JsonResponse(data)