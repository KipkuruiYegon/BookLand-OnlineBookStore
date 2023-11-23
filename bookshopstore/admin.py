from django.contrib import admin

# Register your models here.

from . models import Category
from . models import Book
from . models import Customer
from . models import Order

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
