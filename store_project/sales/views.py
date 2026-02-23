from django.shortcuts import render, redirect
from inventory.models import Product
from .models import Order


def shop(request):
    products = Product.objects.all()
    return render(request, 'sales/shop.html',
                  {'products': products})


def buy_product(request, pk):
    product = Product.objects.get(pk=pk)

    qty = 1
    total = product.price * qty

    Order.objects.create(
        customer=request.user,
        product=product,
        quantity=qty,
        total_price=total
    )

    return redirect('shop')