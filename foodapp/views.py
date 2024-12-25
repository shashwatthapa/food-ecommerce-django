from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
# Create your views here.
def register(request):
    form = RegistrationForm()
    return render(request,"register.html",{"form":form})
def login_view(request):
    form = LoginForm()
    return render(request,"login.html",{"form":form})