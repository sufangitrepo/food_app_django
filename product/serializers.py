from django.conf import settings
from urllib.parse import urlparse
from rest_framework import serializers
from .models import (
    Category,
    Product,
    FavouriteProducts,
    Charges
    )

from app_authentication.serializer import UserDetailSerializer


class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        
        


    def create(self, validated_data):
        image = validated_data.pop('image')
        prod_name = validated_data['product_name']
        product = Product.objects.create(**validated_data)
        product.image = f'images/{prod_name}/{image.name}'
        product.save()
        return product
    
    
    def update(self, instance, validated_data):
        img  = validated_data.pop('image', None)
        product: Product = super().update(instance, validated_data)
        if img is not None:
           product.image = f'images/{product.product_name}/{img.name}'
           product.save()
        return product
    

class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charges
        fields = '__all__'
        


class FavouriteSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = FavouriteProducts
        fields =  ['product', 'user']


class FetchFavouriteSerializer(FavouriteSerializer):
    
   
    product = ProductSerializer()

    class Meta(FavouriteSerializer.Meta):
        fields = ['id', 'product']
