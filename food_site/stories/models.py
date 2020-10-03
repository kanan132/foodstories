from django.db import models
# from django.contrib import get_user_info


# class ArticleSingle(models.Model):
#     title = models.CharField(max_length=150, null=False)
#     text = models.TextField(null=False)


class Recipe(models.Model):
    STATUS_CHOICES=(
        ('male', ("male")),
        ('female', ("female"))
    )

    title = models.CharField(max_length=100)
    short_dscrp = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    # choice = models.CharField(max_length=50,choices=STATUS_CHOICES,default='male')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,db_index=True,related_name='recipe')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    tag = models.CharField(max_length=150)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

