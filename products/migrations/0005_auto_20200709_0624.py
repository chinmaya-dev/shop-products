# Generated by Django 3.0.8 on 2020-07-09 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200709_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_details', to='products.Product'),
        ),
    ]
