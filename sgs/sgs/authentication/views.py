from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,"authentication/index.html")



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        

        myuser.save()
        
        messages.success(request,"Your account has been created.")

        return redirect("signin")

        




    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not none:
            login(request,user)
            firstname=user.firstname
            return render(request,"authentication/index.html",{'fname':firstname})
        else:
            messages.error(request,"bad credintials")
            return redirect("home")

    return render(request,"authentication/signin.html")


def signout(request):
    pass