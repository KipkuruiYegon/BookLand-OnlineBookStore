from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from bookshopstore.models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm


# Create your views here.


def signup_Page(request):
    return render(request, 'authentication/register_account.html')


def register_account(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('/shopper_users/signin_Page/')
        else:
            messages.error(request, "Error")
            return redirect('/shopper_users/register_account/')
    else:
        form = SignupForm()
    return render(request, 'authentication/register_account.html', {'form': form})


def signin_Page(request):
    return render(request, 'authentication/login_account.html')


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


def logout_account(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect("/shopper_users/signin_Page/")


def myaccount(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    return render(request, 'authentication/myaccount.html',  {'cartItems': cartItems})
