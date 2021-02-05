from django.urls import path

from basketapp.views import basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    path('basket-add//<int:product_id>/', basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_remove, name='basket_remove'),
]