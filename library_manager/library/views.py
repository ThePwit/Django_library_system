from re import template
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, CreateView
from .models import LibraryAuthor, LibraryBooks
from .forms import AddBook

# Create your views here.
def book_list(request):
    """
    Display list of all entrys in :model:'LibraryBooks',
    
    books: Querying the database for available data in LibraryBooks table
    
    :template: 'library/book_list.html'    
    """
    books = LibraryBooks.objects.all()
    return render(request, 'library/book_list.html', {'books' : books})

class BookDetailView(DetailView):
    """
    Display details of requested book,
    
    model: 'LibraryBooks' Our table for books with all necessary information
    
    :template: 'library/book_details.html'    
    """
    model = LibraryBooks
    template_name = "library/book_details.html"
    context_object_name = "book"
    
class AddBookView(CreateView):
    """
    Accesses a form to add new books to the database,
    
    :model: 'LibraryBooks' Our table for books
    
    :form: 'AddBook' form with required fields
    
    :template: 'add_books.html'    
    """
    model = LibraryBooks
    form_class = AddBook
    template_name = 'add_book.html'
    success_url = '/book_list/'
