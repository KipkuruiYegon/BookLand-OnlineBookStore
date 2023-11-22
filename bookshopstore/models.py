from django.db import models
import datetime

# Create your models here.

#Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



# Product Book model
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True, default='', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1,  max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=100, default=0, decimal_places=2, blank=False)
    image = models.ImageField(upload_to='bookcovers', default='cover.jpg')
    publishDate = models.CharField(max_length=100, blank=False)
    ISBN = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

#Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.book





