# Generated by Django 4.0.4 on 2022-05-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='item_type',
            field=models.CharField(choices=[('EQUIPMENTS', 'Equipamentos'), ('POTIONS', 'Poções'), ('ITEMS', 'Items')], default='ITEMS', max_length=10),
        ),
    ]
