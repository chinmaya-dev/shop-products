# Generated by Django 3.0.8 on 2020-07-09 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200709_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='products.Product'),
        ),
    ]