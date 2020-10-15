from django.contrib import admin
from stories.models import Recipe, Category, Contact, Subscribe

admin.site.register([Recipe, Category, Contact, Subscribe])
