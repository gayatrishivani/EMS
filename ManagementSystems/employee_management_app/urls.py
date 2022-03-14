from unicodedata import name
from wsgiref.simple_server import demo_app
from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginPage, name='login'),
    path('dologin', DoLogin, name='dologin'),
    path('logout',Logout, name="logout"),
    path('home', HomePage, name="homePage"),
    path('signup', Signup, name="signup")
]
