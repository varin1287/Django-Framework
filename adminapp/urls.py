from django.urls import path

from adminapp.views import index, admins_user_read, admins_user_create


app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admins-user-read/', admins_user_read, name='admins_user_read'),
    path('admins-user-create/', admins_user_create, name='admins_user_create'),
]


