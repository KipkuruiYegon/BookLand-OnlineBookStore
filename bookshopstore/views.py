from django.shortcuts import render
from .models import Book

# Create your views here.


def home(request):
    bookItem = Book.objects.all().order_by('?')
    return render(request, 'home.html', {'bookItem':bookItem})

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def books(request):
    return render(request, 'books.html')

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

