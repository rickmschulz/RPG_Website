# Generated by Django 4.0.4 on 2022-05-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='item_type',
            field=models.CharField(blank=True, choices=[('Armas', (('melee', 'Melee'), ('ranged', 'Ranged')))], max_length=50),
        ),
    ]