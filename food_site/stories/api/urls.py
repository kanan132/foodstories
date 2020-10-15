from django.urls import path
from .views import SubscribeAPI

app_name = 'stories-api'

urlpatterns = [
    path('subscribe/', SubscribeAPI.as_view(), name='subscribe'),
]
