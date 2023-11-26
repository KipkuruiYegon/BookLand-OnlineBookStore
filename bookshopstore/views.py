from django.shortcuts import render,redirect
from .models import Book, Category, Blog
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    book = Book.objects.all().order_by('?')
    return render(request, 'home.html', {'book': book, 'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def news(request):
    return render(request, 'news.html')


def bookcollection(request):
    book = Book.objects.all().order_by('?')
    category = Category.objects.all().order_by('?')
    return render(request, 'bookcollection.html', {'book': book, 'category': category, 'navbar': 'bookcollection'})


def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_details.html', {'book': book})


def category_books_collection(request, id):
    category = Category.objects.get(id=id)
    book = Book.objects.filter(category=category)
    return render(request, 'category_books_collection.html', {'category': category, 'book': book})


def addbook_cart(request, id):
    return render(request, 'cart.html')


def removebook_cart(request, id):
    return render(request, 'cart.html')


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_details.html', {'blog': blog})


def cart(request):
    return render(request, 'cart.html', {'navbar': 'cart'})


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog, 'navbar': 'blog'})


def checkout(request):
    return render(request, 'checkout.html', {'navbar': 'checkout'})

def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def errorpage(request):
    return render(request, '404page.html')
