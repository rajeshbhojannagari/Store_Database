from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=18)
    address=models.TextField()
    def __str__(self):
        return self.user.username

class Order(models.Model):
    customer=models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    def __str__(self):
        return f"order #{self.id}-{self.customer.user.username}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"{self.product.name} {self.quantity}"
# Create your models here.
