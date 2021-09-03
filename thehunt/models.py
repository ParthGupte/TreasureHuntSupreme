from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)