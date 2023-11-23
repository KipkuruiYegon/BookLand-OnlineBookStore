from django.shortcuts import render
from .models import Book

# Create your views here.


def home(request):
    bookItem = Book.objects.all().order_by('?')
    return render(request, 'home.html', {'bookItem':bookItem, 'navbar':'home'})

def about(request):
    return render(request, 'about.html', {'navbar':'about'})

def news(request):
    return render(request, 'news.html')

def bookcollection(request):
    return render(request, 'bookcollection.html', {'navbar':'bookcollection'})

def book_details(request):
    return render(request, 'book_details.html', {'navbar':'book_details'})

def blog_details(request):
    return render(request, 'blog_details.html' )

def cart(request):
    return render(request, 'cart.html', {'navbar':'cart'})

def blog(request):
    return render(request, 'blog.html', {'navbar':'blog'})

def checkout(request):
    return render(request, 'checkout.html', {'navbar':'checkout'})

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

def thankyou(request):
    return render(request, 'thankyou.html')
def contact(request):
    return render(request, 'contact.html', {'navbar':'contact'})
def errorpage(request):
    return render(request, '404page.html')

