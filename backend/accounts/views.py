from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, SignInForm
from accounts.models import CustomUser  


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "auth/sign_up.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = SignInForm()
    return render(request, "auth/sign_in.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect("home")
