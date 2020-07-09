from django.shortcuts import render
from products.models import Shop, Category, Product, Media
from products.serializers import ShopSerializer, ProductSerializer, CategorySerializer, MediaSerializer
from rest_framework import viewsets
from rest_framework.renderers import BaseRenderer, JSONRenderer
from rest_framework.utils import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

class ProductsViewSet(viewsets.ModelViewSet):   
    
    queryset = Category.objects.prefetch_related('products')
    serializer_class = CategorySerializer
    def retrieve(self,request,pk):        
        
         queryset = Category.objects.prefetch_related('products').filter(shop_id=pk)        
         if not queryset:
             return Response({"status":status.HTTP_404_NOT_FOUND,"message":"No Shop details found"})
         else:
             serializer = CategorySerializer(queryset,many=True)
             return Response({"status":status.HTTP_200_OK,"data":serializer.data,"message":"Products Retrieved Successfully."})
   