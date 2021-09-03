from django.shortcuts import render
from thehunt.models import *
# Create your views here.

def home(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    if User.objects.exists(username=username):
        objlist = User.objects.get(username=username)
        if password == objlist[0][2]:
            return render(request,'main.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    


