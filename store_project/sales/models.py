from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product


class Order(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)