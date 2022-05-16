from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
    # overriding using form fields
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'style': 'display: block',
                                          'placeholder': 'Your description of the item',
                                          'class': 'new-class-name two',
                                          'id': 'my-id-for-textarea',
                                          'rows': 6,
                                          'cols': 60
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

# 1 - equipamento
#  1.1 - armas
#   1.1.1 - melee
#   1.1.2 - ranged
#  2.1 - armaduras
#   2.1.1 - helmet
#   2.1.2 - body-armor
#   2.1.3 - acessórios
#     2.1.1.1 - amuleto
#     2.1.1.2 - anel
#     2.1.1.3 - capas
#     2.1.1.4 - braceletes
#     2.1.1.5 - botas
# 3 - consumíveis
#   3.1 - poções
#   3.2 - scrolls
#   3.3 - varinhas
#   3.4 - outros.
#      3.4.1 - input livre
