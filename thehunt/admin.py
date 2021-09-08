from django.contrib import admin
from .models import Users, GlobalVariables, Questions
# Register your models here.

admin.site.register(Users)
admin.site.register(GlobalVariables)
admin.site.register(Questions)