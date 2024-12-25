from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import PostItem
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        label = "Email"
     
    )
    class Meta:
        model = User
        fields =  ["username","email","password1","password2"]

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput()
        
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput()
    )
    
class Post(forms.ModelForm):
    class Meta:
        model = PostItem
        fields = ["name","image","price"]
        