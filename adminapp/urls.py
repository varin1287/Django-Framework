from django.urls import path

from adminapp import views


app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admins-user-read/', views.admins_user_read, name='admins_user_read'),
    path('admins-user-create/', views.admins_user_create, name='admins_user_create'),
    path('admins-user-update/<int:id>/', views.admins_user_update, name='admins_user_update'),
    path('admins-user-delete/<int:id>/', views.admins_user_delete, name='admins_user_delete'),
    path('admins-products-read/', views.admin_products_read, name='admin_products_read'),
    path('admins-products-create/', views.admins_products_create, name='admins_products_create'),
    path('admins-products-update/<int:id>/', views.admins_products_update, name='admins_products_update'),
    path('admins-products-delete/<int:id>/', views.admins_products_delete, name='admins_products_delete'),
]


