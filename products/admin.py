from django.contrib import admin
from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time', 'is_enable']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'category', 'is_enable']
    list_filter = ['category']
    search_fields = ['name', 'category']
