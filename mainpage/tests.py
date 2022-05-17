from django.test import TestCase

# Create your tests here.
filter_groups = ['Melee', 'Ranged', 'Helmet', 'Body Armor', 'Amuletos', 'Anéis', 'Botas', 'Braceletes', 'Capas',
                     'Poções', 'Scrolls', 'Varinhas']

chained_filters = {}
i = 0
for filted_group in filter_groups:
    chained_filters[f'key{i}'] = f'Inventory.objects.filter(item_type={filted_group})'
    i += 1

print(chained_filters)
print(chained_filters.get('key1'))