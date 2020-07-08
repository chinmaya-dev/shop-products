from django.db import models

# Create your models here.
class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    shop_name = models.TextField()
    shop_location = models.TextField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField()
    parent_Category = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField()

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    category_id = models.IntegerField()
    
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    product_image = models.TextField()