from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from thehunt.models import *
# Create your views here.

def home(request):
    return render(request,'login.html',{"msg":""})

def register(request):

    return render(request,'register.html')

def process_registration(request):
    Fullname = request.POST['fullname'].lstrip().rstrip()
    Fullname2 = request.POST['fullname2'].lstrip().rstrip()
    Iiserid = request.POST['iiserid'].lstrip().rstrip()
    Username = request.POST['username'].lstrip().rstrip()
    Password = request.POST['password']
    Cpassword = request.POST['cpassword']
    if Password != Cpassword:
        return render(request,'register.html',{'msg':'Passwords do not match'})
    elif Fullname=='' or Iiserid=='' or Username=='' or Password=='':
        return render(request,'register.html',{'msg':'Mandatory fields cannot be empty'})

    else:
        b = Users(fullname=Fullname,fullname2=Fullname2, iiserid=Iiserid, username=Username, password=Password)
        b.save()



    return redirect('home')
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    objlist = Users.objects.filter(username=username)
    if objlist.exists():
        if objlist.first()[password] == password:
            return render(request,'main.html')
        else:
            return render(request, 'login.html',{"msg":"Incorrect Username or Password"})
    else:
        return render(request, 'login.html',{"msg":"Incorrect Username or Password"})
    
