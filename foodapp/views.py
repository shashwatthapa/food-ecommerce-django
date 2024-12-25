from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm,Post
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import PostItem
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("login")
        else:
            return render(request,"register.html",{"form":form,"error":"Invalid credentials"})
    else:
        form = RegistrationForm()
        return render(request,"register.html",{"form":form})    
    return render(request,"register.html",{"form":form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,"login.html",{"form":form,"error":"Invalid credentials"})
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    
@login_required
def home(request):
    return render(request,'home.html')

def logout_views(request):
    logout(request)
    return redirect('login')

def products(request):
    mem = PostItem.objects.all()
    return render(request,"product.html",{"mem":mem})

def carts(request):
    pass

def main(request):
    mem = PostItem.objects.all()
    return render(request,"main.html",{"mem":mem})



def add(request):
    if request.method == 'POST':
        form = Post(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return render(request,'add.html',{"form":form})
    else:
        form = Post()
        return render(request,'add.html',{"form":form})


def delete(request,id):
    mem = PostItem.objects.get(id=id)
    mem.delete()
    return redirect('main')

def update(request,id):
    mem = PostItem.objects.get(id=id)
    if request.method == 'POST':
        form = Post(request.POST,instance=mem)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = Post(instance=mem)
        return render(request,"update.html",{"form":form,"mem":mem})
