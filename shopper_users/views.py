from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms


# Create your views here.
def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Account Created Successfully")
        return redirect('/shopper_users/signin_Page/')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register_account.html', {'form': form})


def login_account(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("/shopper_users/signin_Page/")
        else:
            messages.success(request, "Invalid username or password")
            return redirect("/shopper_users/signin_Page/")

    return render(request, 'authentication/login_account.html', {'navbar': 'login_account'})


def signup_Page(request):
    return render(request, 'authentication/register_account.html')


def signin_Page(request):
    return render(request, 'authentication/login_account.html')


def logout_account(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect("/shopper_users/signin_Page/")


def myaccount(request):
    return render(request, 'authentication/myaccount.html')
