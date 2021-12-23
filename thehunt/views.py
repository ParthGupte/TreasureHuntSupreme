from django.contrib.auth.models import User
from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from thehunt.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import datetime
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.email_is_verified:
            return render(request,'main.html',{'username':request.user.username})
        else:
            return render(request,'login.html',{"msg":"Your email is not verified yet, please check your email."})
    else:
        return render(request,'login.html',{"msg":""})

def register(request):

    return render(request,'register.html')

def process_registration(request):
    Fullname = request.POST['fullname'].lstrip().rstrip()
    # Fullname2 = request.POST['fullname2'].lstrip().rstrip()
    Iiserid = request.POST['iiserid'].lstrip().rstrip()
    Username = request.POST['username'].lstrip().rstrip()
    Password = str(request.POST['password'])
    Cpassword = str(request.POST['cpassword'])
    if Password != Cpassword:
        return render(request,'register.html',{'msg':'Passwords do not match'})
    elif Fullname=='' or Iiserid=='' or Username=='' or Password=='':
        return render(request,'register.html',{'msg':'Mandatory fields cannot be empty'})

    else:
        try:
            b = Users.objects.create_user(fullname=Fullname, iiserid=Iiserid, username=Username, password=Password)
            b.save()
            send_email(b, request)
        except:
            return render(request,'register.html',{'msg':'There was an error please try again or contact tech support'})
        else:
            return redirect('home')


# login method has been imported now. Usage: login(request, user)

# def login(username):
#     user = Users.objects.filter(username=username).first()
#     user.log = True

#logout method usage: logout(request)

# def logout(username):
#     user = Users.objects.filter(username=username).first()
#     user.log = False

"""def loginrequired(username):
    user = Users.objects.filter(username=username).first()
    if user.log:
        pass
    else:
        return redirect('home')"""


def login_view(request):
    username = str(request.POST['username'])
    password = str(request.POST['password'])

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.email_is_verified:
            login(request, user)
            return render(request,'main.html',{'username':username})
        else:
            return render(request,'login.html',{"msg":"Your email is not verified yet, please check your email."})
    else:
        return render(request, 'login.html',{"msg":"Incorrect Username or Password"})

@login_required(login_url='/')
def hunt(request):
    now = timezone.now()
    username = request.user.username
    test_start = GlobalVariables.objects.get(pk=1).test_start
    test_end = GlobalVariables.objects.get(pk=1).test_end
    if test_start<= now <= test_end:
        return redirect('level')
    elif test_start>now:
        return render(request,'main.html',{'msg':'Please wait for the Treasure hunt to start'})
    else:
        return render(request,'main.html',{'msg':'Treasure Hunt has already ended','username':username})


@login_required(login_url='/')
def level(request):
    user = request.user
    username = user.username
    lvl = user.lvl
    questionobj = Questions.objects.filter(lvl=lvl).first() 
    if questionobj is not None:
        question = questionobj.question
        return render(request,'lvl.html',{'username':username,'question':question,'lvl':lvl,'questionobj':questionobj})
    else:
        return redirect('leaderboard')

@login_required(login_url='/')
def leaderboard(request):
    now = timezone.now()
    test_start = GlobalVariables.objects.get(pk=1).test_start
    if test_start<= now:
        ranked_users = Users.objects.order_by('-lvl', 'lastlvl_time').exclude(lvl=1)
        return render(request, 'leaderboard.html',{'ranked_users':ranked_users})
    else:
        return redirect('home')


@login_required(login_url='/')
def checkans(request):
    now = timezone.now()
    user = request.user
    lvl = user.lvl
    ans = Questions.objects.get(lvl=lvl).modelanswer
    user_answer = request.POST['answer']
    end_time = GlobalVariables.objects.get(pk=1).test_end
    if end_time<now:
        return render(request,'leaderboard.html',{{'msg':'Time ended so your last answer was not recorded'}})
    elif user_answer.lstrip().rstrip().lower()== ans.lstrip().rstrip().lower():
        user.lvl = lvl+1
        user.lastlvl_time = timezone.now()
        user.save()
        return redirect('level')
    else:
        return redirect('level')

def logout_view(request):
    logout(request)
    return redirect('home')

'''class table(TemplateView):
      template_name = 'table.html'

      def get_context_data(self, **kwargs):
            ctx = super(table, self).get_context_data(**kwargs)
            ctx['header'] = ['#', 'Username','Level','Last Level Time']
            ctx['rows'] = [{'id':1, 'chemblid':534988,'prefName':'A'},
                           {'id':2, 'chemblid':31290,'prefName':'B'},
                           {'id':3, 'chemblid':98765,'prefName':'C'}]
            return ctx'''

#def changepswd(request):
#    email = request.POST['iiserid']
#    password = request.Post['password']
#    try:
#        user = Users.objects.get(iiserid=email)
#    except:
#        return render(request,'changepswd.html',{'msg':"Email id doesn't exist"})
#    else:
#        user.set_password(password)
#        return render(request,'changepswd.html',{'msg':'Password changed'})

def send_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate Conquestar account'
    email_body = render_to_string('activate.html',{
        'user':user, 
        'domain':current_site, 
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
        })
    
    email = EmailMessage(subject=email_subject,body=email_body,from_email=settings.EMAIL_FROM_USER,to=[user.iiserid])
    email.send()

def activate_user(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
    
    if user and generate_token.check_token(user,token):
        user.email_is_verified = True
        user.save()
        messages.add_message(request,messages.SUCCESS,'Email verified, you can proceed to login')
        return redirect('home')
    return render(request,'activate-failed.html',{'user':user})

