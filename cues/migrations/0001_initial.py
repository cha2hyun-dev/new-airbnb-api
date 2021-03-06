# Generated by Django 3.1b1 on 2020-09-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('isButt', models.BooleanField(default=False)),
                ('isShaft', models.BooleanField(default=False)),
                ('productBrand', models.CharField(default=False, max_length=140)),
                ('productName', models.CharField(default=False, max_length=140)),
                ('productNumber', models.CharField(blank=True, default=False, max_length=140)),
                ('purchasedCustomer', models.CharField(max_length=140)),
                ('purchasedCustomerProtectedName', models.CharField(blank=True, max_length=140)),
                ('purchasedDate', models.DateTimeField(auto_now_add=True)),
                ('warrantyNumber', models.CharField(blank=True, max_length=140)),
                ('warrantyDate', models.DateTimeField(blank=True)),
                ('warrantyManager', models.CharField(max_length=140)),
                ('count', models.IntegerField(blank=True, default=0)),
                ('lastView', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
