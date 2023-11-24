from django.contrib import admin

# Register your models here.

from . models import Category
from . models import Book
from . models import Customer
from . models import Order
from . models import Review
from . models import Blog
from . models import MessageInquiry
from . models import CommentBlog
from . models import Feedback

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Blog)
admin.site.register(MessageInquiry)
admin.site.register(CommentBlog)
admin.site.register(Feedback)
