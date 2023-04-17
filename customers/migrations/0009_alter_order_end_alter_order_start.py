# Generated by Django 4.1.2 on 2022-11-01 00:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]