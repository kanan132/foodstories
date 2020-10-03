from django.db import models

class Register(models.Model):
    STATUS_CHOICES=(
        (1, ("male")),
        (2, ("female"))
    )
    
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    choice = models.CharField(max_length=10,choices=STATUS_CHOICES,default=1)
    
