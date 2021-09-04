from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    fullname2 = models.CharField(max_length=50, unique=True, default='')
    iiserid = models.TextField(unique=True)
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=10)
    lvl = models.IntegerField(default=1)