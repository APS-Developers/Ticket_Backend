# Generated by Django 3.2 on 2022-07-02 20:13

import datetime
from django.db import migrations, models
import inventory.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_csvs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Item_dispatched_Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Orgnization_Id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Purchase_Date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Slip',
            field=models.FileField(null=True, upload_to='', validators=[inventory.validators.validate_file_extension]),
        ),
    ]
