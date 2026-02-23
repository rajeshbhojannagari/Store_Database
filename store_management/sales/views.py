from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from inventory.models import Product
from .models import Customer,Order,OrderItem
from .forms import OrderItemForm

#checkcustomer
def customer_required(user):
    return user.profile.role=='customer'

#productbrowsing
@login_required
def product_catalog(request):
    if not customer_required(request.user):
        return redirect('seller_dashboard')
    products=Product.objects.all()
    return render(request,'sales/product_catalog.html',{'products':products})

#createorder
def create_order(request):
    if not customer_required(request.user):
        return redirect('seller_dashboard')
    customer,created=Customer.objects.get_or_create(user=request.user)
    if request.method=='POST':
        form=OrderItemForm(request.POST)
        if form.is_valid():
            product=form.cleaned_data['product']
            quantity=form.cleaned_data['quantity']
            order=Order.objects.create(customer=customer)
            total=product.price*quantity
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
                )
            order.total_amount=total
            order.save()
            product.stock-=quantity
            product.save()
            return redirect('order_success')
    else:
        form=OrderItemForm()
    return render(request,'sales/create_order.html',{'form':form})

#successpage
@login_required
def order_success(request):
    return render(request,'sales/order_success.html')
# Create your views here.
