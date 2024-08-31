from django.shortcuts import render, redirect
from .forms import RegistrationForm, LogingForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        
    return render(request, 'main/register.html', {'form':form})

def login(request):
    form = LogingForm()
    if request.method == "POST":
        form = LogingForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')

    return render(request, 'main/login.html', {'form':form})

def logout_user(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/login')
