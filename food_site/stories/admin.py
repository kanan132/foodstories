from django.contrib import admin
from stories.models import Recipe, Category, Contact

admin.site.register([Recipe, Category, Contact])
