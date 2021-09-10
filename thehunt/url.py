from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login_view',views.login_view, name='login_view'),
    path('register',views.register, name='register'),
    path('process_registration',views.process_registration,name="process_registration"),
    path('hunt',views.hunt,name='hunt'),
    path('leaderboard',views.leaderboard,name='leaderboard'),
    path('level',views.level, name='level'),
    path('checkans',views.checkans, name='checkans'),
    path('logout_view',views.logout_view, name='logout_view'),
   # path('changepswd',views.changepswd, name='changepswd')
    ]