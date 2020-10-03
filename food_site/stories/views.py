from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from stories.models import Recipe, Category
from django.views.generic import ListView

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

