from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from stories.models import Recipe, Category
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .forms import ContactForm, CreateStoryForm

# def recipe(request):
#     recipes = Recipe.objects.all()
#     context = {"recipes": recipes}
#     return render(request,'templates/recipes.html',context)


class RecipeListView(ListView):

    model = Recipe
    context_object_name = "recipes"
    queryset=Recipe.objects.all()
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = "now"
        return context


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('stories:contact')


class CreateStoryView(CreateView):
    form_class = CreateStoryForm
    template_name = 'create_story.html'
    success_url = reverse_lazy('stories:create_story')

class AboutView(TemplateView):
    template_name = 'about.html'

class IndexView():
    pass

