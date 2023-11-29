from django.contrib.auth.models import User
from django.db import models
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, blank=False)
    image = models.ImageField(upload_to='bookcovers', default='cover.jpg')
    publishDate = models.DateField(max_length=100, blank=False)
    ISBN = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title

    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total



class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    def __str__(self):
        return self.country


# Customer model
class ShippingDetail(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)


class SliderHome(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sliders', default='avatar.jpg', blank="False")

    def __str__(self):
        return self.name


class Socialfollow(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='socials', default='avatar.jpg')

    def __str__(self):
        return self.name


class PromoPageImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='promo', default='avatar.jpg')

    def __str__(self):
        return self.name


# Cart model


# Book review model
class ReviewBook(models.Model):
    shopper = models.ForeignKey(User, on_delete=models.CASCADE, )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    description = models.CharField(max_length=2000, blank=True, default='', null=True)
    rating = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.shopper


# Message contact model
class MessageContactsection(models.Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True, default='', null=True)
    body = models.CharField(max_length=2000, blank=True, default='', null=True)

    def __str__(self):
        return self.username


class TagTrend(models.Model):
    tagitem = models.CharField(max_length=200, default='', blank=False)

    def __str__(self):
        return self.tagitem


# Blog model
class Blog(models.Model):
    tag = models.ForeignKey(TagTrend, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to='blogs', default='blog.jpg')

    def __str__(self):
        return self.tag


# Blog comments model
class CommentBlog(models.Model):
    shopper = models.ForeignKey(User, on_delete=models.CASCADE, )
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True, default='', null=True)
    body = models.CharField(max_length=2000, blank=True, default='', null=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.username


class FeedbackTestimonial(models.Model):
    shopper = models.ForeignKey(User, on_delete=models.CASCADE, )
    body = models.CharField(max_length=2000, blank=True)
    satisfaction = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.shopper
