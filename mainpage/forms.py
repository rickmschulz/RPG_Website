from django import forms

from .models import Inventory

class RawInventoryForm(forms.Form):
    EQUIPMENTS = 'EQUIPMENTS'
    POTIONS = 'POTIONS'
    ITEMS = 'ITEMS'
    item_choices = [
        (EQUIPMENTS, 'Equipamentos'),
        (POTIONS, 'Poções'),
        (ITEMS, 'Items')
    ]
    item_type = forms.ChoiceField(choices=item_choices)
    description = forms.CharField()
    quantity = forms.IntegerField()


