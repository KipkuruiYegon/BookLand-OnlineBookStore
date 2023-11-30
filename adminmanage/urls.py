from django.urls import path
from . import views

app_name = "adminmanage"

urlpatterns = [
    path('', views.adminpage, name="adminpage"),
    path('adminadd_book/', views.add_book, name="add_book"),
    path('view_book_list/', views.view_book_list, name="view_book_list"),
    path('view_book_details/<id>/', views.view_book_details, name="view_book_details"),
    path('edit_book_item/<id>', views.edit_book_item, name="edit_book_item")

]