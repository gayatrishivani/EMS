from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

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
            return redirect("/home")
        #HttpResponse("Email:"+request.POST.get("username")+ " password : "+request.POST.get("password") )
        else:
            return HttpResponse("Invalid login")

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