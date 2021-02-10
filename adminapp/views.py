from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import AdminUserRegisterForm, AdminUserProfileForm

def index(request):
    return render(request, 'adminapp/index.html')

def admins_user_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admins_user_read.html', context)

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

