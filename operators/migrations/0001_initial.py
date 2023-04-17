# Generated by Django 4.1.2 on 2022-11-04 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Operator",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=60, unique=True)),
                ("password", models.CharField(max_length=30)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={"verbose_name_plural": "Operators",},
        ),
    ]