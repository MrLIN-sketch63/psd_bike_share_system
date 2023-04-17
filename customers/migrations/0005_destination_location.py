# Generated by Django 4.1.2 on 2022-10-31 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_vehicle_location_repair_hirebike'),
    ]

    operations = [
        migrations.CreateModel(
            name='destination_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(default='', max_length=20)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
    ]
