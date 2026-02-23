from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=18)
    email=models.EmailField(blank=True)
    address=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True) 
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    supplier=models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
