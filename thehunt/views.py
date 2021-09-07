from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from thehunt.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
import datetime
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
        b = Users.objects.create_user(fullname=Fullname,fullname2=Fullname2, iiserid=Iiserid, username=Username, password=Password)
        return redirect('home')


# login method has been imported now. Usage: login(request, user)

# def login(username):
#     user = Users.objects.filter(username=username).first()
#     user.log = True

#logout method usage: logout(request)

# def logout(username):
#     user = Users.objects.filter(username=username).first()
#     user.log = False

def loginrequired(username):
    user = Users.objects.filter(username=username).first()
    if user.log:
        pass
    else:
        return redirect('home')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'main.html')
    else:
        return render(request, 'login.html',{"msg":"Incorrect Username or Password"})


def hunt(request):
    now = timezone.now()
    test_start = now #GlobalVariables.objects.get(pk=1).test_start
    test_end = now+datetime.timedelta(seconds=9999999) #GlobalVariables.objects.get(pk=1).test_end
    if test_start<= now <= test_end:
        return redirect('level')
    elif test_start<now:
        return render(request,'main.html',{'msg':'Please wait for the Treasure hunt to start'})

def level(request):
    return render(request,'lvl.html')


def leaderboard(request):
    return render(request, 'leaderboard.html')
