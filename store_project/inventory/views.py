from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.filter(seller=request.user)
    return render(request,
                  'inventory/product_list.html',
                  {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request,
                  'inventory/add_product.html',
                  {'form': form})