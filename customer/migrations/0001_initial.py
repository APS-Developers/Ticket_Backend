# Generated by Django 3.2 on 2022-06-29 16:50

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('OrgID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('ContactNo', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Contact No')),
                ('EmailAddress', models.EmailField(blank=True, max_length=200, verbose_name='Email Address')),
                ('Address', models.TextField(max_length=200, verbose_name='Address')),
            ],
            options={
                'db_table': 'Organisation',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('ContactNo', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Contact No')),
                ('EmailAddress', models.EmailField(blank=True, max_length=200, verbose_name='Email Address')),
                ('Organisation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.organisation')),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]