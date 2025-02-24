from django.shortcuts import render
from .models import Book, Author,BookInstance
from django.views import generic


def index(request):
    """View function for home page of site."""

    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)  
    num_visits += 1  
    request.session['num_visits'] = num_visits 

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits, 
    }

    return render(request, 'index.html', context=context)

# Book List View
class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  

# Book Detail View
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'  

# Author List View
class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10  # Paginate results

# Author Detail View
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
