from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import Product
from adminapp.forms import AdminUserRegisterForm, AdminUserProfileForm, AdminProductsRegisterForm, AdminProductsProfileForm

@user_passes_test(lambda u: u.is_superuser, login_url='mainapp:products')
def index(request):
    return render(request, 'adminapp/index.html')

# Пользователи
@user_passes_test(lambda u: u.is_superuser)
def admins_user_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admins_user_read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_user_create(request):
    if request.method == 'POST':
        form = AdminUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_user_read'))
    else:
        form = AdminUserRegisterForm()
    context = {'form': form, }
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_user_update(request, id=None):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = AdminUserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_user_read'))
    else:
        form = AdminUserProfileForm(instance=user)
    context = {'current_user': user,
               'form': form,
               }
    return render(request, 'adminapp/admin_user_update_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admins_user_read'))

# Продукты
@user_passes_test(lambda u: u.is_superuser)
def admin_products_read(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin_products_read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_products_create(request):
    if request.method == 'POST':
        form = AdminProductsRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = AdminProductsRegisterForm()
    context = {'form': form, }
    return render(request, 'adminapp/admin_products_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_products_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductsProfileForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = AdminProductsProfileForm(instance=product)
    context = {'current_product': product,
               'form': form,
               }
    return render(request, 'adminapp/admins_products_update_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admins_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products_read'))







