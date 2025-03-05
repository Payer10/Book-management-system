from django.urls import path
from .views import*

urlpatterns = [
    path('',homepage,name='homepage'),
    path("add_book/",add_book, name="add_book"),
    path('delete/<int:book_id>',delete_book,name="delete_book")
    path('edit/<int:book_id>',edit_book,name="edit_book")
]