from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirm password',
                'class' : 'form-control',
             }))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'id':'first_name','placeholder':'First name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'id':'last_name','placeholder':'Last name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'id':'username','placeholder':'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id':'email','placeholder':'Email', 'class': 'form-control'}),
        }









