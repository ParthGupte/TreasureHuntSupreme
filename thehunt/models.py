from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    fullname = models.CharField(max_length=50, unique=True, blank=False)
    fullname2 = models.CharField(max_length=50, unique=True, blank=True)
    iiserid = models.CharField(blank=False, max_length=70)
    username = models.CharField(max_length=10, unique=True, blank=False)
    password = models.CharField(max_length=10, blank=False)
    log = models.BooleanField(default=False)
    lvl = models.IntegerField(default=1)

class GlobalVariables(models.Model):
    test_start = models.DateTimeField()
    test_end = models.DateTimeField()
