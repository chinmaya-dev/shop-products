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
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')  
    
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='details')
    product_image = models.TextField()
    
    