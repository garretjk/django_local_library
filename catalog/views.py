from django.shortcuts import render
from .models import Book, Author

def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')

def book_list(request):
    """View function for displaying all books."""
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def author_list(request):
    """View function for displaying all authors."""
    authors = Author.objects.all()
    return render(request, 'catalog/author_list.html', {'authors': authors})
