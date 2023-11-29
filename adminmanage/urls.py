from django.urls import path
from . import views

app_name = "adminmanage"

urlpatterns = [
    path('', views.adminpage, name="adminpage"),
    path('add_book/', views.add_book, name="add_book")

]