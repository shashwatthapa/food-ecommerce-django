from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.
def register(request):
    form = RegistrationForm()
    return render(request,"register.html",{"form":form})