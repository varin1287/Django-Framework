from django.shortcuts import render

from mainapp.models import Product, ProductCategory

def index(request):
    context = {
        'head': 'geekShop - главная',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, id=None):
    context = {
        'head': 'geekShop - каталог',
        'menu_names': ProductCategory.objects.all(),
        'cards': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

