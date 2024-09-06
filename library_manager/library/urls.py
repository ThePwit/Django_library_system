from django.urls import path
from . import views
from .views import BookDetailView, AddBookView
   
urlpatterns = [
    path("book_details/<int:pk>/", BookDetailView.as_view(), name="book_details"),
    path('book_list/', views.book_list, name='book_list'),
    path('book_list/create/', AddBookView.as_view(), name='add_book'),
]
