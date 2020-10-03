from django.urls import path

from .views import RecipeListView

app_name = "stories"

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe'),

]