from django.db import models
# from django.contrib import get_user_info

from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     GENDER_CHOICES = (
#     ("Male", ("Male")),
#     ("Female", ("Female"))
# )
#     bio = models.TextField(max_length=1000, blank=True)
#     profile_img = models.ImageField(upload_to='images')
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=6)

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'



class Recipe(models.Model):

    title = models.CharField(max_length=100)
    short_dscrp = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    # choice = models.CharField(max_length=50,choices=STATUS_CHOICES,default='male')
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,db_index=True,related_name='recipe')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"


class Category(models.Model):
    tag = models.CharField(max_length=150)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Comments(models.Model):
    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='comments')
    description = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"