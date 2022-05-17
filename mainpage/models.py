from django.db import models
from django.urls import reverse

# Create your models here.
class Inventory(models.Model):
    item_choices = [
        ('Armas', (
            ('Melee', 'Melee'),
            ('Ranged', 'Ranged')
        )),
        ('Armaduras', (
            ('Helmet', 'Helmet'),
            ('Body Armor', 'Body Armor'),
        )),
        ('Acessórios', (
            ('Amuletos', 'Amuletos'),
            ('Anéis', 'Anéis'),
            ('Capas', 'Capas'),
            ('Braceletes', 'Braceletes'),
            ('Botas', 'Botas')
        )),
        ('Consumíveis', (
            ('Poções', 'Poções'),
            ('Scrolls', 'Scrolls'),
            ('Varinhas', 'Varinhas'),
        )),
        ('Outros', (
            ('Input Livre', 'Input Livre'),
        ))
    ]
    item_type = models.CharField(max_length=20, choices=item_choices, blank=False)
    description = models.CharField(max_length=300, blank=True)
    quantity = models.IntegerField()

    # another method for absolute url
    def get_absolute_url(self):
        return reverse('mainpage:inventory-lookup', kwargs={"id": self.id})    # hardcoded method f"/inventory/{self.id}/"

