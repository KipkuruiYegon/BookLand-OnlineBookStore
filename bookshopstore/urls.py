from django.urls import path
from . import views

app_name = "bookshopstore"
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),
    path('errorpage/', views.errorpage, name="errorpage"),
    path('bookcollection/', views.bookcollection, name="bookcollection"),
    path('book_details/<id>/', views.book_details, name="book_details"),
    path('blog_details/<id>/', views.blog_details, name="blog_details"),
    path('category_books_collection/<id>/', views.category_books_collection, name="category_books_collection"),
    path('cart/', views.cart, name="cart"),
    path('addbook_cart/', views.addbook_cart, name="addbook_cart"),
    path('removebook_cart/', views.removebook_cart, name="removebook_cart"),
    path('blog/', views.blog, name="blog"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_account/', views.login_account, name="login_account"),
    path('register_account/', views.register_account, name="register_account"),
    path('logout_account/', views.logout_account, name="logout_account"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('thankyou/', views.thankyou, name="thankyou")
]