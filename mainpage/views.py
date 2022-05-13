from django.shortcuts import render
from .forms import RawInventoryForm
from .models import Inventory

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inventory(request):
    my_form = RawInventoryForm()
    if request.method == 'POST':
        my_form = RawInventoryForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Inventory.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'inventory.html', context)
