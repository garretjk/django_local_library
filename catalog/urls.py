from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Book URLs
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Author URLs
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
