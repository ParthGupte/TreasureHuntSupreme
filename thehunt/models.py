from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Users(AbstractUser):
    fullname = models.CharField(max_length=50, unique=True, blank=False)
    #fullname2 = models.CharField(max_length=50, blank=True)
    iiserid = models.CharField(blank=False, max_length=70)
    username = models.CharField(max_length=10, unique=True, blank=False)
    password = models.TextField(blank=False)
    log = models.BooleanField(default=False)
    lvl = models.IntegerField(default=1)
    lastlvl_time = models.DateTimeField(default='2021-09-08 00:00:00')

class GlobalVariables(models.Model):
    test_start = models.DateTimeField()
    test_end = models.DateTimeField()
    test_dur = models.DurationField()

class Questions(models.Model):
    lvl = models.IntegerField(primary_key=True)
    imgpath = models.TextField()
    question = models.TextField()
    #modelanswer = models.TextField()

class Answers(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    lvl = models.ForeignKey(Questions, on_delete=models.CASCADE)
    ans = models.TextField()
