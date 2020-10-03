from django.contrib import admin
from stories.models import Recipe, Category

admin.site.register([Recipe, Category])
