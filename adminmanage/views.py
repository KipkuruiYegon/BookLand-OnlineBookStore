from django.shortcuts import render, redirect
from bookshopstore.models import Category, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def adminpage(request):
    return render(request, 'index.html')


def view_book_list(request):
    book = Book.objects.all()
    return render(request, 'view_book_list.html', {'book': book})


def view_book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'view_book_details.html', {'book': book})
def edit_book_item(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')
        ISBN = request.POST.get('ISBN')
        publishDate = request.POST.get('publishDate')
        image = request.FILES['image']

# get the id to display the data
        book = Book.objects.get(id=id)
        book.title = title
        book.description = description
        book.category_id = category_id
        book.publisher = publisher
        book.price = price
        book.ISBN = ISBN
        book.publishDate = publishDate
        book.image = image

# check if the image is already selected by default or not
# replace the image
        if len(request.FILES) != 0:
            if len(book.image) > 0:
                book.image = request.FILES['image']

        book.save()
        messages.success(request, 'Book Changes updated Successfully!')

    return render(request, 'book_edit.html', {'book': book})

def add_book(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')
        ISBN = request.POST.get('ISBN')
        publishDate = request.POST.get('publishDate')
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        # this function will overwrite the image path but will not delete the previous picture
        if image:
            book = Book(title=title, author=author, description=description, image=image, category=category,
                        publisher=publisher, price=price, ISBN=ISBN, publishDate=publishDate)
        book.save()
        messages.success(request, 'Book added successfully, Add another item')
        return render(request, 'add_book.html')

    return render(request, 'add_book.html', {'categories': categories})
