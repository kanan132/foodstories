from django.urls import path

from .views import RecipeListView, ContactView, AboutView, CreateStoryView, IndexView

app_name = "stories"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', RecipeListView.as_view(), name='recipe'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('create-story/', CreateStoryView.as_view(), name='create_story'),
    path('about/', AboutView.as_view(), name='about'),
    

]