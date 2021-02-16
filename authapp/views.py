from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from basketapp.models import Basket
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User



class UserLoginView(LoginView):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm


class UserCreateView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

class UserProfileView(UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        self.success_url = reverse_lazy('auth:profile', args=[self.kwargs['pk']])
        return str(self.success_url)




# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('auth:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {'head': 'GeekShop - Профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#                }
#     return render(request, 'authapp/profile.html', context)


