from django.urls import path

from mainapp.views import index, products


app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:category_id>/', products, name='product'),
    path('products/page/<int:page>/', products, name='product_page'),
    path('products/<int:category_id>/page/<int:page>/', products, name='category_page'),
]


