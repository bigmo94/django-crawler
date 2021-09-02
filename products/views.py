from django.shortcuts import render, get_object_or_404

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
