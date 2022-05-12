from django.shortcuts import render
from .forms import RawInventoryForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inventory(request):
    my_form = RawInventoryForm()
    context = {
        'form': my_form
    }
    return render(request, 'inventory.html', context)
