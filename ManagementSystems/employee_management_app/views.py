from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.urls import reverse

from .models import CustomUser

from .authen import Authen

# Create your views here.

def HomePage(request):
    return render(request, 'app/home.html')

def LoginPage(request):
    return render(request, 'login.html')

def DoLogin(request):
    if request.method !='POST':
        return HttpResponse("<h2> Method not Allowed </h2>")
    else:
        user = Authen.authenticate(request,username= request.POST.get("username"), password= request.POST.get("password"))
        if user != None:
            login(request, user)
            print("login done", user)
            if (user.user_type == "1"):
                return HttpResponseRedirect("/admin-home")
            elif (user.user_type == "2"):
                return HttpResponseRedirect('/home')
        #HttpResponse("Email:"+request.POST.get("username")+ " password : "+request.POST.get("password") )
        else:
            return HttpResponse("Invalid login")

def admin_view(request):
    return render(request, 'admin/admin-base.html')

def staff_view(request):
    pass

def Profile(request):
    if request.user !=None:
        return HttpResponse("User: "+request.user.username)
    else:
        return HttpResponse("Please login")

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def Signup(request):
    
    return render(request, 'signup.html')

def doSignup(request):
    if request.method != "POST":
        return HttpResponse("Method is not allowed")
    else:
        username = request.POST.get("username")
        email = request.POST.get("emailid")
        password =request.POST.get("password1")
        is_staff = request.POST.get("is_staff")
        print(username, email, password, is_staff)



def Add_staff(request):
    return render (request, 'admin/add_staff.html')

def Adding_staff(request):
    if request.method != 'POST':
        return HttpResponse("Method not allowed!")
    
    else:
        first_name = request.POST.get("Firstname")
        last_name = request.POST.get("Lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        emailid = request.POST.get("emailid")
        staff = request.POST.get("is_staff")
        gender = request.POST.get("gender")
        is_staff = True
        
        if staff is None:
            is_staff == False
        
        print('this worked once')
        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=emailid,last_name=last_name,first_name=first_name,user_type=2)
            print(user)
            print(CustomUser.objects.create)
            user.save()
            return HttpResponseRedirect("/add_staff")
        except:
            return HttpResponse("error in adding try again")


