from django.shortcuts import render
from accounts.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from accounts.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'stories:recipe'


