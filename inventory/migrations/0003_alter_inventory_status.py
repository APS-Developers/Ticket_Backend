# Generated by Django 3.2 on 2022-06-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Status',
            field=models.IntegerField(choices=[(0, 'Working'), (1, 'Not Working')], verbose_name='Status'),
        ),
    ]
