from django.urls import path
from .import views

urlpatterns=[
    path('',views.product_catalog,name='product_catalog'),
    path('order/',views.create_order,name='create_order'),
    path('success/',views.order_success,name='order_success')
]