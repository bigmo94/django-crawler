from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from .serializer import CategorySerializer, ProductSerializer
from .models import Category, Product


def category_list(request):
    category = Category.objects.all()
    context = {'categories': category}
    return render(request, "products/category_list.html", context)


def product_list(request, category_id):
    products = Product.objects.filter(category__id=category_id)
    context = {'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
