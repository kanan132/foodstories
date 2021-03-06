from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
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



class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'username',
                'placeholder': 'Your Username',
                'class': 'form-control'
            }))

    class Meta:
        model = User
        fields = ['username', 'password']




class ResetItDown(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-control',
        })
    )

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
             }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-control',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )











