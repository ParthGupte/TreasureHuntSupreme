from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('process_registration',views.process_registration,name="process_registration")
    ]