from unicodedata import name
from wsgiref.simple_server import demo_app
from django.urls import path

from .admin_views import client_view

from .staff_views import *
from .views import *

app_name = "main_app"
urlpatterns = [
    path('', LoginPage, name='login'),
    path('dologin', DoLogin, name='dologin'),
    path('logout',Logout, name="logout"),
    path('home', HomePage, name="homePage"),
    path('signup', Signup, name="signup"),
    path('doSignup', doSignup, name="doSignUp"),
    path('attendance', Attendance_show, name="attendance"),
    path('mark_attendance', mark_attendance, name = "mark_attendance"),
    path('request_leave',request_leave, name="request_leave"),
    #admins
    path('admin-home', admin_view, name="adminHome"),
    path('add_staff',Add_staff, name = "add_staff"),
    path('adding_staff', Adding_staff, name="adding_staff"),
    path('client', client_view, name='client'),

]
