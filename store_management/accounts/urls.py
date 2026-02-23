from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_view,name='login'),
    path('register/',views.Register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('seller/',views.seller_dashboard,name='seller_dashboard'),
    path('customer/',views.customer_dashboard,name='customer_dashboard')
]