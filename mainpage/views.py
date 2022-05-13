from django.shortcuts import render
from .forms import InventoryForm
from .models import Inventory

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inventory(request):
    initial_data = {
        'description': 'This is my awesome item!'
    }
    form = InventoryForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = InventoryForm

    context = {
        'form': form
    }
    return render(request, 'inventory.html', context)
