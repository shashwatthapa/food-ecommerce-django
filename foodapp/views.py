from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
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
