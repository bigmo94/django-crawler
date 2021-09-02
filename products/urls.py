from django.urls import path
from .views import category_list, product_list, product_detail

app_name = 'products'

urlpatterns = [
    path('category-list/', category_list, name='category_list'),
    path('product-list/<int:category_id>/', product_list, name="product_list"),
    path('product-detail/<int:product_id>/', product_detail, name='product_detail')
]
