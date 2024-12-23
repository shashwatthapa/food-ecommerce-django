from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm,PostItem
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import FoodItems
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'registration.html',{'form':form,'error':'Invalid credentials'})
    else:
        form = RegistrationForm()
        return render(request,'registration.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                return render(request,'login.html',{'form':form,'error':'Invalid credentials'})
            
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def main(request):
    mem = FoodItems.objects.all().order_by('-id')
    return render(request,'admin.html',{'mem':mem})

def add(request):
    if request.method == 'POST':
        form = PostItem(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
       

    else:
        form = PostItem()
        return render(request,'add.html',{'form':form})