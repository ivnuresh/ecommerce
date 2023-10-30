from . import views
from django.urls import path

app_name = 'cartapp'

urlpatterns = [
     path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
     path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
]


