from django.shortcuts import render
from .models import Book, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


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
    return render(request, 'category_books_collection.html',{'category': category, 'book': book})

def blog_details(request):
    return render(request, 'blog_details.html')


def cart(request):
    return render(request, 'cart.html', {'navbar': 'cart'})


def blog(request):
    return render(request, 'blog.html', {'navbar': 'blog'})


def checkout(request):
    return render(request, 'checkout.html', {'navbar': 'checkout'})


def signup(request):
    return render(request, 'login_signUp.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def errorpage(request):
    return render(request, '404page.html')


def loginaccount(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("/")
        else:
            messages.success(request, "Error Logging in")
            return redirect("/loginaccount")

    return render(request, 'authentication/login_signUp.html', {'navbar': 'loginaccount'})


def signupaccount(request):
    return render(request, 'authentication/login_signUp.html')


def logoutaccount(request):
    logout(request)
    messages.success(request, "Logged Out Successfully, Please Login to continue shopping")
    return redirect("/loginaccount")


def myaccount(request):
    return render(request, 'authentication/myaccount.html')
