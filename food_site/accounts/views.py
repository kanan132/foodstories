from django.shortcuts import render
from accounts.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from accounts.forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'stories:recipe'


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class ResetPasswordView(PasswordResetView):
    form_class = ResetItDown
    template_view = 'forget_password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'


class ResetPasswordConfirmView(PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm
    template_name= "reset_password.html" 
    success_url = reverse_lazy('accounts:login')
    

# class ProfileView(DetailView):
#     model = User
#     template_name = 'user-profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context