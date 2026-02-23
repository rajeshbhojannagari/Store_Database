from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

#Register
def Register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            role=form.cleaned_data['role']
            profile=user.profile
            profile.role=role
            profile.save()
            messages.success(request,"Account created")
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

#login
def login_view(request):
    if request.method=='POST':
        username=request.POST.get['username']
        password=request.POST.get['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            role=user.profile.role
            if role=='seller':
                return redirect('seller_dashboard')
            elif role=='customer':
                return redirect('customer_dashboard')
        else:
            messages.error(request,"Invalid Details Please check your username and password")
    return render(request,'accounts/login.html')

#logout
def logout_view(request):
    logout(request)
    return redirect('login')

#dashboard
@login_required
def seller_dashboard(request):
    if request.user.profile.role!='seller':
        return redirect('customer_dashboard')
    return render(request,'accounts/seller_dashboard.html')
@login_required
def customer_dashboard(request):
    if request.user.profile.role!='customer':
        return redirect('seller_dashboard')
    return render(request,'accounts/customer_dashboard.html')

# Create your views here.
