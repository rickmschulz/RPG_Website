from django.shortcuts import render, get_object_or_404, redirect
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
        form = InventoryForm(initial=initial_data)

    context = {
        'form': form
    }
    return render(request, 'inventory.html', context)


def inventory_update_view(request, id=id):
    obj = get_object_or_404(Inventory, id=id)
    form = InventoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'inventory.html', context)


def inventory_list_view(request):
    queryset = Inventory.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, 'inventory_list.html', context)


def inventory_lookup_view(request, id):
    # obj = Inventory.objects.get(id=id)
    obj = get_object_or_404(Inventory, id=id)

    context = {
        "object": obj
    }
    return render(request, 'inventory_lookup.html', context)


def delete_view(request, id):
    # obj = Inventory.objects.get(id=id)
    obj = get_object_or_404(Inventory, id=id)
    # POST request
    if request.method == 'POST':
        #confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'inventory_delete.html', context)
