# Generated by Django 4.2.6 on 2023-10-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='allergens',
            field=models.ManyToManyField(blank=True, null=True, to='orders.allergen'),
        ),
    ]