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
    path('book_details/', views.book_details, name="book_details"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('cart/', views.cart, name="cart"),
    path('blog/', views.blog, name="blog"),
    path('checkout/', views.checkout, name="checkout"),
    path('loginaccount/', views.loginaccount, name="loginaccount"),
    path('signupaccount/', views.signupaccount, name="signupaccount"),
    path('logoutaccount/', views.logoutaccount, name="logoutaccount"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('thankyou/', views.thankyou, name="thankyou")
]