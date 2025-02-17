from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home Page
    path('books/', views.book_list, name='book-list'),
    path('authors/', views.author_list, name='author-list'),
]
