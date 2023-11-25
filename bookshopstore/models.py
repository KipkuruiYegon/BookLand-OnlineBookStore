from django.db import models
import datetime


# Create your models here.

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Product Book model
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    description = models.TextField( blank=True, default='', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, blank=False)
    image = models.ImageField(upload_to='bookcovers', default='cover.jpg')
    publishDate = models.CharField(max_length=100, blank=False)
    ISBN = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    def __str__(self):
        return self.country
# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='customers', default='avatar.jpg')

    def __str__(self):
        return self.first_name


# Cart model
class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)


# Order model
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default='')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=100, default='', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book

# Book review model
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    description = models.CharField(max_length=2000, blank=True, default='', null=True)
    rating = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.customer


# Message contact model
class MessageInquiry(models.Model):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True, default='', null=True)
    body = models.CharField(max_length=2000, blank=True, default='', null=True)

    def __str__(self):
        return self.username

class Tag(models.Model):
    tag_name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.tag_name
# Blog model
class Blog(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    image = models.ImageField(upload_to='blogs', default='blog.jpg')

    def __str__(self):
        return self.title


# Blog comments model
class CommentBlog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True, default='', null=True)
    body = models.CharField(max_length=2000, blank=True, default='', null=True)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.username


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    body = models.CharField(max_length=2000, blank=True)
    satisfaction = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.customer
