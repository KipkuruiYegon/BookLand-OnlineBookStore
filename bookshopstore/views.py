from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse, HttpResponse
import json
# for query handling
from django.db.models import Q
import datetime
from django.utils import timezone

from django.contrib import messages


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    book = Book.objects.all().order_by('?')
    slider = SliderHome.objects.all().order_by('?')
    socialFollow = Socialfollow.objects.all().order_by('?')
    promo = PromoPageImage.objects.all().order_by('?')
    categories = Category.objects.all()

    return render(request, 'home.html',
                  {'book': book, 'slider': slider, 'socialFollow': socialFollow, 'promo': promo, 'cartItems': cartItems,
                   'categories': categories, 'navbar': 'home'})


def about(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    categories = Category.objects.all()
    socialFollow = Socialfollow.objects.all().order_by('?')
    return render(request, 'about.html', {'categories': categories, 'socialFollow':socialFollow, 'cartItems': cartItems, 'navbar': 'about'})


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
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    book = Book.objects.all()
    category = Category.objects.all().order_by('?')
    categories = Category.objects.all()
    socialFollow = Socialfollow.objects.all().order_by('?')
    return render(request, 'bookcollection.html',
                  {'book': book, 'items': items, 'socialFollow': socialFollow, 'category': category,
                   'cartItems': cartItems, 'categories': categories,
                   'navbar': 'bookcollection'})


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
    categories = Category.objects.all()
    return render(request, 'category_books_collection.html',
                  {'category': category, 'categories': categories, 'book': book})


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
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
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
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    return render(request, 'checkout.html', {'items': items, 'order': order, 'cartItems': cartItems, 'navbar': 'cart'})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            # check characters typed in both lower and upper case in the search bar
            book = Book.objects.all().filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query) | Q(
                    publishDate__icontains=query) | Q(ISBN__icontains=query))
            category = Category.objects.all().filter(Q(name__icontains=query))

            return render(request, 'search.html', {'book': book, 'category': category, 'query': query})

        return render(request, 'search.html')


def adminDashboard(request):
    return render(request, 'admin/index.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    categories = Category.objects.all()
    return render(request, 'contact.html', {'categories': categories, 'cartItems': cartItems, 'navbar': 'contact'})


def errorpage(request):
    return render(request, '404page.html')


def processOrder(request):
    print('Data:', request.body)
    return JsonResponse('Order was Placed', safe=False)


def placeorder(request):
    if request.method == 'POST':
        user = request.user
        form_data = request.POST

        # Extract form data
        shipping_name = form_data['name']
        email = form_data['email']
        state = form_data['state']
        address = form_data['address']
        city = form_data['city']
        zipcode = form_data['zipcode']
        phone = form_data['phone']
        transaction_code = form_data['transaction_code']

        # Update Customer info
        if user.is_authenticated:
            user.first_name, user.last_name = shipping_name.split(" ", 1)
            user.email = email
            user.save()

        # Update or create ShippingAddress
        shipping_address, created = ShippingAddress.objects.get_or_create(
            customer=user,
            defaults={
                'city': city,
                'address': address,
                'state': state,
                'zipcode': zipcode,
                'phone': phone,
            }
        )
        if not created:
            shipping_address.city = city
            shipping_address.address = address
            shipping_address.state = state
            shipping_address.zipcode = zipcode
            shipping_address.phone = phone
            shipping_address.save()

        # Update Order info
        order = Order.objects.get(customer=user, completed=False)
        order.transaction_id = transaction_code
        order.completed = True
        order.date_ordered = timezone.now()
        order.save()

        # Update OrderItems
        order_items = OrderItem.objects.filter(order=order)
        for item in order_items:
            item.book.on_sale = False  # Assuming on_sale should be set to False after completing the order
            item.book.save()

        # Reset user's cart
        order.orderitem_set.all().delete()

        messages.success(request, 'Your order has been placed successfully!')
        return redirect('/cart')

    else:
        return redirect('shopper_users:myaccount')
