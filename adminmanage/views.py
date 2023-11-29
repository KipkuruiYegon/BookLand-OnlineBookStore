from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.



def adminpage(request):
    return render(request, 'index.html')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        category = request.FILES['category']
        publisher = request.FILES['publisher']
        price = request.FILES['image']
        ISBN = request.FILES['ISBN']
        date = request.FILES['date']
        image = request.FILES['image']

        # this function will overwrite the image path but will not delete the previous picture
        if len(request.FILES) != 0:
            image = request.FILES['image']

        book = Book(title=title, author=author, description=description, image=image, category=category, publisher=publisher, price=price, ISBN=ISBN, date=date,)
        book.save()
        messages.success(request, 'Book added successfully')
        return redirect("/add_book")

    return redirect("/add_book")
