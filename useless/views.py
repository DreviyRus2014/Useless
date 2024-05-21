from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import django.contrib.auth
from django.contrib.auth.models import User


@login_required()
def home(request):
    return render(request,"home.html",{})

def login(request):
    context={}
    if request.method == "POST":

        user = django.contrib.auth.authenticate(request)

        if user:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
        context["invalid"] = True

    return render(request, "login.html", context)


def register(request):

    authenticated = request.user.is_authenticated
    
    if request.method == "POST" and not authenticated:
        user = User.objects.create_user(request.POST["username"])
        user.save()
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('addpasskey'))
    
    if authenticated:
        return HttpResponseRedirect(reverse('home'))
    
    return render(request,"register.html",{})


def add_passkey(request):
    return render(request,"addpasskey.html",{})


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('login'))
