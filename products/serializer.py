from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'seller', 'color', 'category']


class CategorySerializer(serializers.ModelSerializer):
    product_list = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'created_time', 'updated_time', 'product_list']
