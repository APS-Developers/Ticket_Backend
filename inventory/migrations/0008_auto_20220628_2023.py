# Generated by Django 3.2 on 2022-06-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_inventory_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='Slip',
        ),
        migrations.AddField(
            model_name='inventory',
            name='Status',
            field=models.CharField(blank=True, choices=[('Working', 'Working'), ('Not Working', 'Not Working')], max_length=20, null=True),
        ),
    ]
