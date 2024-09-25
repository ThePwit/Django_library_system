from re import template
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_required
from .models import LibraryAuthor, LibraryBooks
from .forms import AddBook

# Create your views here.
def home(request):
    
    return (request, 'home.html')

def book_list(request):
    """
    Display list of all entrys in :model:'LibraryBooks',
    
    books: Querying the database for available data in LibraryBooks table
    
    :template: 'library/book_list.html'    
    """
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    books = LibraryBooks.objects.all()
    
    return render(request, 'library/book_list.html', {'books' : books, 'count': count})

class BookDetailView(DetailView):
    """
    Display details of requested book,
    
    model: 'LibraryBooks' Our table for books with all necessary information
    
    :template: 'library/book_details.html'    
    """
    model = LibraryBooks
    template_name = "library/book_details.html"
    context_object_name = "book"
    
    
'''class AddBookView(CreateView):
    
    Accesses a form to add new books to the database,
    
    :model: 'LibraryBooks' Our table for books
    
    :form: 'AddBook' form with required fields
    
    :template: 'add_books.html'    
    
    model = LibraryBooks
    form_class = AddBook
    template_name = 'add_book.html'
    success_url = '/book_list/' 
    '''
    
@login_required    
def AddBookView(request):
    """
    Accesses a form to add new books to the database,
    
    :model: 'LibraryBooks' Our table for books
    
    :form: 'AddBook' form with required fields
    
    :template: 'add_books.html'    
    """
    form = AddBook(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/book_list/')
    return render(request,'add_book.html', {'form': form})
    
