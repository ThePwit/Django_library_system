from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
def home(request):
    #request.session.set_test_cookie()
    #request.session['userid'] = User.id
    #request.session.save()
    
    return render(request, 'home.html')
    
    
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
        
        return Response({'count': count, 'book': book})
    
    
class BookList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request):
        count = request.session.get('count', 0)
        count += 1
        request.session['count'] = count
        books = LibraryBooks.objects.all()
        serializer = BookSerializer(books, many=True)
    
        return Response({'books': books, 'count': count}, None, 'library/book_list.html')
        
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(template_name = 'add_book.html')
