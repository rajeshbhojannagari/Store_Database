from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('buy/<int:pk>/', views.buy_product,
         name='buy_product'),
]