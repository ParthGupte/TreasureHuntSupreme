from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=50, unique=True, blank=False)
    fullname2 = models.CharField(max_length=50, unique=True, blank=True)
    iiserid = models.CharField(blank=False, max_length=70)
    username = models.CharField(max_length=10, unique=True, blank=False)
    password = models.CharField(max_length=10, blank=False)
    lvl = models.IntegerField(default=1) 