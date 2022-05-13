from django import forms

from .models import Inventory

class InventoryForm(forms.ModelForm):
    EQUIPMENTS = 'EQUIPMENTS'
    POTIONS = 'POTIONS'
    ITEMS = 'ITEMS'
    item_choices = [
        (EQUIPMENTS, 'Equipamentos'),
        (POTIONS, 'Poções'),
        (ITEMS, 'Items')
    ]
    # overriding form fields
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'style': 'display: block',
                                          'placeholder': 'Your description of the item',
                                          'class': 'new-class-name two',
                                          'id': 'my-id-for-textarea',
                                          'rows': 10,
                                          'cols': 80
                                      }
                                  ))
    quantity = forms.IntegerField()

    class Meta:
        model = Inventory
        fields = [
            'item_type',
            'description',
            'quantity'
        ]
    # Validation forms
    # def clean_description(self, *args, **kwargs):
    #     description = self.cleaned_data.get('description')
    #     if 'TESTE' not in description:
    #         raise forms.ValidationError('This is not a valid description!')
    #     return description

