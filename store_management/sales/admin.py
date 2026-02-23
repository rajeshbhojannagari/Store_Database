from django.contrib import admin
from .models import Customer,Order,OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','total_amount','created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','product','quantity','price']
# Register your models here.
