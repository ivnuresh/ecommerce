from . import views
from django.urls import path

app_name = 'shoppingapp'

urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('<slug:c_slug>/', views.allproducts, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.proDetails, name='proDetails')
]
