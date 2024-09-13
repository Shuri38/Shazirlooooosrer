from django.shortcuts import render,  get_object_or_404,redirect
from .models import Inventaires, Armes, Skins
#from .forms import InventoryForm, WeaponForm, SkinForm
from django.contrib.auth.models import User

# Create your views here.
def accueil(request):
    return render(request, 'public/index.html') #important de préciser le public


def inventory_list(request):
    inventories = Inventaires.objects.all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def weapon_list(request, inventory_id):
    inventory = get_object_or_404(Inventaires, id=inventory_id)
    weapons = inventory.weapons.all()
    return render(request, 'weapon_list.html', {'inventory': inventory, 'weapons': weapons})

def skin_list(request, weapon_id):
    weapon = get_object_or_404(Armes, id=weapon_id)
    skins = weapon.skins.all()
    return render(request, 'skin_list.html', {'weapon': weapon, 'skins': skins})

def create_inventory(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        user = User.objects.get(id=user_id)
        Inventaires.objects.create(user=user)
        return redirect('inventory_list')
    users = User.objects.all()
    return render(request, 'create_inventory.html', {'users': users})

def create_weapon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weapon_type = request.POST.get('weapon_type')
        damage = request.POST.get('damage')
        inventory_id = request.POST.get('inventory')
        inventory = Inventaires.objects.get(id=inventory_id)
        Armes.objects.create(name=name, weapon_type=weapon_type, damage=damage, inventory=inventory)
        return redirect('weapon_list', inventory_id=inventory_id)
    inventories = Inventaires.objects.all()
    return render(request, 'create_weapon.html', {'inventories': inventories})

def create_skin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rarity = request.POST.get('rarity')
        weapon_id = request.POST.get('weapon')
        weapon = Armes.objects.get(id=weapon_id)
        image = request.FILES.get('image')
        Skins.objects.create(name=name, rarity=rarity, weapon=weapon, image=image)
        return redirect('skin_list', weapon_id=weapon_id)
    weapons = Armes.objects.all()
    return render(request, 'create_skin.html', {'weapons': weapons})