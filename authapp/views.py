from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from basketapp.models import Basket
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {'form': form, 'head': 'авторизация'}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form, 'head': 'регистрация'}
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    context = {'head': 'GeekShop - Профиль',
               'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               'total_quantity': sum(basket.quantity for basket in baskets),
               'total_sum': sum(basket.sum() for basket in baskets),
               }
    return render(request, 'authapp/profile.html', context)


