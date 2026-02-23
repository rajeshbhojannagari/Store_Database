from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

#sellercheck
def seller_required(user):
    return user.profile.role=='seller'

#productlist
@login_required
def product_list(request):
    if not seller_required(request.user):
        return redirect('customer_dashboard')
    products=Product.objects.all()
    return render(request,'inventory/product_list.html',{'products':products})

#addproduct
@login_required
def add_product(request):
    if not seller_required(request.user):
        return redirect('customer_dashboard')
    form=ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'inventory/add_product.html',{'form':form})

#updateproduct
@login_required
def update_product(request,pk):
    if not seller_required(request.user):
        return redirect('customer_dashboard')
    product=get_object_or_404(Product,pk=pk)
    form=ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'inventory/update_product.html',{'form':form})

#deleteproduct
@login_required
def delete_product(request,pk):
    if not seller_required(request.user):
        return redirect('customer_dashboard')
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request,'inventory/delete_product.html',{'product':product})

# Create your views here.
