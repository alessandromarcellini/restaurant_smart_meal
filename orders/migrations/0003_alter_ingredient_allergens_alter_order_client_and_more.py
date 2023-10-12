# Generated by Django 4.2.6 on 2023-10-12 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_client_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='allergens',
            field=models.ManyToManyField(null=True, to='orders.allergen'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.client'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, to='orders.order'),
        ),
    ]