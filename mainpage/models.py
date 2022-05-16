from django.db import models
from django.urls import reverse

# Create your models here.
class Inventory(models.Model):
    item_choices = [
        ('Armas', (
            ('melee', 'Melee'),
            ('ranged', 'Ranged')
        )),
        ('Armaduras', (
            ('helmet', 'Helmet'),
            ('body armor', 'Body Armor'),
        )),
        ('Acessórios', (
            ('amuletos', 'Amuletos'),
            ('anéis', 'Anéis'),
            ('capas', 'Capas'),
            ('braceletes', 'Braceletes'),
            ('botas', 'Botas')
        )),
        ('Consumíveis', (
            ('poções', 'Poções'),
            ('scrolls', 'Scrolls'),
            ('varinhas', 'Varinhas'),
        )),
        ('Outros', (
            ('input livre', 'Input Livre'),
        ))
    ]
    item_type = models.CharField(max_length=20, choices=item_choices, blank=False)
    description = models.CharField(max_length=300, blank=True)
    quantity = models.IntegerField()

    # another method for absolute url
    def get_absolute_url(self):
        return reverse('mainpage:inventory-lookup', kwargs={"id": self.id})    # hardcoded method f"/inventory/{self.id}/"

