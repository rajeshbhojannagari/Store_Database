from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    image = models.ImageField(upload_to='products/',
                              blank=True, null=True)