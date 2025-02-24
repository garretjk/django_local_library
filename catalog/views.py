from django.shortcuts import render
from .models import Book, Author
from django.views import generic


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

# Book List View
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10  # Paginate results to 10 per page

# Book Detail View
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10  # Paginate results

class AuthorDetailView(generic.DetailView):
    model = Author

