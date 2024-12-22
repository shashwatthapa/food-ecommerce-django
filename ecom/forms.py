from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import password_validators_help_texts


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={'class':'form-control'}),
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')

    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text='<ul>' + ''.join([f'<li>{text}</li>' for text in password_validators_help_texts()]) + '</ul>')

    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        help_text = 'You must enter same password you entered above.')


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(attrs={'class':'form-control'}))
    

