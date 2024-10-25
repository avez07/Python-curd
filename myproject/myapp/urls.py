
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList,name='bookList'),
      path('new/', views.book_create, name='book_create'),
]
