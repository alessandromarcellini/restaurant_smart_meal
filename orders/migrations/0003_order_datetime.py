# Generated by Django 4.2.6 on 2023-10-25 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_client_allergens_alter_ingredient_allergens'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 25, 18, 48, 43, 555430)),
        ),
    ]
