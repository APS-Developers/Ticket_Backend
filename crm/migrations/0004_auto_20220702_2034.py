# Generated by Django 3.2 on 2022-07-02 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20220630_1331'),
        ('crm', '0003_auto_20220702_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='FaultFoundCode',
            field=models.CharField(blank=True, choices=[('Router', 'Router faulty'), ('Modem', 'Modem faulty'), ('Switch', 'Switch faulty')], max_length=30, verbose_name='Fault Found Code'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ResolutionCode',
            field=models.CharField(blank=True, choices=[('123', 'Router faulty'), ('456', 'Modem faulty')], max_length=20, verbose_name='Resolution Code'),
        ),
    ]
