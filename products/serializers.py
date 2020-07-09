from rest_framework_json_api import serializers
from products.models import Shop, Category, Product, Media
from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json
from collections import OrderedDict

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('id')

class MediaSerializer(serializers.HyperlinkedModelSerializer):      
    class Meta:
        model = Media
        fields = ('product_image')

class ProductSerializer(serializers.HyperlinkedModelSerializer):    
    product_image = serializers.SerializerMethodField()   
    class Meta:
        model = Product
        fields = ('id', 'product_name','product_image')
    
    def get_product_image(self, obj):
        queryset = Media.objects.values('product_image').filter(
            product_id=obj.id).first()         
        return queryset
    
    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        categoryList = data.pop('product_image')
        for key, val in categoryList.items():
            data.update({key: val})
        return data 

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True)    
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'products')
    


  

