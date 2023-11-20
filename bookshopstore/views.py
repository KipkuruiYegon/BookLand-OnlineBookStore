from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def shop(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

def thankyou(request):
    return render(request, 'thankyou.html')
def contact(request):
    return render(request, 'contact.html')
def errorpage(request):
    return render(request, '404page.html')

