from django.db import models

# Create your models here.
class Inventory(models.Model):
    EQUIPMENTS = 'EQ'
    POTIONS = 'POT'
    ITEMS = 'IT'
    item_choices = [
        (EQUIPMENTS, 'Equipamentos'),
        (POTIONS, 'Poções'),
        (ITEMS, 'Items')
    ]
    item_type = models.CharField(max_length=3, choices=item_choices, default=ITEMS)
    description = models.CharField(max_length=300, blank=True)
    quantity = models.IntegerField()
