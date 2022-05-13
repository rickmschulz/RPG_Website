from django.db import models

# Create your models here.
class Inventory(models.Model):
    EQUIPMENTS = 'EQUIPMENTS'
    POTIONS = 'POTIONS'
    ITEMS = 'ITEMS'
    item_choices = [
        (EQUIPMENTS, 'Equipamentos'),
        (POTIONS, 'Poções'),
        (ITEMS, 'Items')
    ]
    item_type = models.CharField(max_length=10, choices=item_choices, blank=True)
    description = models.CharField(max_length=300, blank=True)
    quantity = models.IntegerField()
