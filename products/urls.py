from django.urls import path

from .views import (category_list,
                    product_list,
                    product_detail,
                    CategoryListAPIView,
                    ProductsAPIView,
                    ProductDetailAPIView)

app_name = 'products'

urlpatterns = [
    path('category-list/', category_list, name='category_list'),
    path('product-list/<int:category_id>/', product_list, name="product_list"),
    path('product-detail/<int:product_id>/', product_detail, name='product_detail'),
    path('category-api/', CategoryListAPIView.as_view(), name='category_api'),
    path('product-api/', ProductsAPIView.as_view(), name='product-api'),
    path('product-api/<int:id>/', ProductDetailAPIView.as_view(), name='products_detail_api'),
]
