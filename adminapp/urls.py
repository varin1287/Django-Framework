from django.urls import path

from adminapp.views import index, admins_user_read, admins_user_create, admins_user_update, admins_user_delete


app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admins-user-read/', admins_user_read, name='admins_user_read'),
    path('admins-user-create/', admins_user_create, name='admins_user_create'),
    path('admins-user-update/<int:id>', admins_user_update, name='admins_user_update'),
path('admins-user-delete/<int:id>', admins_user_delete, name='admins_user_delete'),
]


