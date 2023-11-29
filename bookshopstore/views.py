from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    book = Book.objects.all().order_by('?')
    slider = SliderHome.objects.all().order_by('?')
    socialFollow = Socialfollow.objects.all().order_by('?')
    promo = PromoPageImage.objects.all().order_by('?')
    return render(request, 'home.html',
                  {'book': book, 'slider': slider, 'socialFollow': socialFollow, 'promo': promo, 'cartItems': cartItems,
                   'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def news(request):
    return render(request, 'news.html')


def bookcollection(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    book = Book.objects.all().order_by('?')
    category = Category.objects.all().order_by('?')
    return render(request, 'bookcollection.html',
                  {'book': book, 'category': category, 'cartItems': cartItems, 'navbar': 'bookcollection'})


def book_details(request, id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    book = Book.objects.get(id=id)
    return render(request, 'book_details.html', {'book': book, 'cartItems': cartItems})


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
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    return render(request, 'cart.html', {'items': items, 'order': order, 'cartItems': cartItems, 'navbar': 'cart'})


def updateItem(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']

    print('Action:', action)
    print('bookId:', bookId)

    customer = request.user
    book = Book.objects.get(id=bookId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, book=book)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog, 'navbar': 'blog'})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    return render(request, 'checkout.html', {'items': items, 'order': order,'cartItems': cartItems, 'navbar': 'cart'})


def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def errorpage(request):
    return render(request, '404page.html')
