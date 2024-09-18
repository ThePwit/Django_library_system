from re import template
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, CreateView
from .models import LibraryAuthor, LibraryBooks
from .forms import AddBook
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status, serializers
from rest_framework.views import APIView
from .serializers import *

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
    
class BookDetails(APIView):
    """
    Display details of requested book,
    
    model: 'LibraryBooks' Our table for books with all necessary information
    
    :template: 'library/book_details.html'    
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'library/book_details.html'
    
    def get(self, request, pk):
        book = get_object_or_404(LibraryBooks, pk=pk)
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})
    
    
class BookList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'library/book_list.html'
    
    def get(self, request):
        books = LibraryBooks.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'serializer': serializer, 'books': books})
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
