from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ("Male", ("Male")),
        ("Female", ("Female"))
    )
    bio = models.TextField(max_length=1000, blank=True)
    profile_img = models.ImageField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    email = models.EmailField(max_length=250)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
