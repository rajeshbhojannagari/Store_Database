from django.contrib import admin
from .models import Category,Supplier,Product

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display=['name','phone','email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','price','stock']
    list_filter=['category']
    search_fields=['name']
# Register your models here.
