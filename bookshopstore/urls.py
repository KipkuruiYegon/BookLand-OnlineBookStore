from django.urls import path
from . import views

app_name = "bookshopstore"
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),
    path('errorpage/', views.errorpage, name="errorpage"),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('thankyou/', views.thankyou, name="thankyou")
]