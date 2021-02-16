from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.models import Product, ProductCategory

def index(request):
    context = {
        'head': 'geekShop - главная',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None, page=1):
    menu_names = ProductCategory.objects.all()

    if not category_id:
        category_name= ''
        cards = Product.objects.all()
    else:
        category_name = ProductCategory.objects.get(id=category_id)
        cards = Product.objects.filter(category=category_name)
    products_on_page = 2
    paginator = Paginator(cards, products_on_page)
    context = {
        'head': 'geekShop - каталог',
        'menu_names': menu_names,
        'cards': paginator.page(page),
        'category_name': category_name,
    }
    return render(request, 'mainapp/products.html', context)





