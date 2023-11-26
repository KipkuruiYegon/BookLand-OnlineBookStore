from django.urls import path
from . import views

app_name = "shopper_users"
urlpatterns = [
    path('', views.signin_Page, name="signin_Page"),
    path('login_account/', views.login_account, name="login_account"),
    path('register_account/', views.register_account, name="register_account"),
    path('logout_account/', views.logout_account, name="logout_account"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('signup_Page/', views.signup_Page, name="signup_Page"),
    path('signin_Page/', views.signin_Page, name="signin_Page")
]