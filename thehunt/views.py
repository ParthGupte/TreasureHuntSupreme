from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from thehunt.models import *
# Create your views here.

def home(request):
    return render(request,'login.html',{"msg":""})

def register(request):

    return render(request,'register.html')

def process_registration(request):
    return HttpResponseRedirect('')
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    objlist = User.objects.filter(username=username)
    if objlist.exists():
        if objlist.first()[password] == password:
            return render(request,'main.html')
        else:
            return render(request, 'login.html',{"msg":"Incorrect Username or Password"})
    else:
        return render(request, 'login.html',{"msg":"Incorrect Username or Password"})
    
