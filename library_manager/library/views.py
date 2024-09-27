from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_not_required, permission_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import LibraryAuthor, LibraryBooks
from .forms import AddBook, UpdateUser
from .serializers import BookSerializer

# Create your views here.
@login_not_required
def home(request):
    
    return (request, 'home.html')

@login_not_required
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

class BookListAPI(APIView):
    
    @method_decorator(permission_required('library.api', '/login/', True ))
    def get(self, request):
        books = LibraryBooks.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        

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
    #success_message = 'Book successfully added to library'
    success_url = '/book_list/' 
     
#def AddBookView(request):
    """
    Accesses a form to add new books to the database,
    
    :model: 'LibraryBooks' Our table for books
    
    :form: 'AddBook' form with required fields
    
    :template: 'add_books.html'    
    """
    #form = AddBook(request.POST or None)
    #if request.method == 'POST':
        #if form.is_valid():
            #form.save()
            #return redirect('/book_list/')
    #return render(request,'add_book.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        form = UpdateUser(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)
    
