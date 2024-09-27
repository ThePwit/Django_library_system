from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/api/', views.BookListAPI.as_view()),
    path('books/create/', views.AddBookView.as_view(), name='add_book'),
    path("book_details/<int:pk>/", views.BookDetailView.as_view(), name="book_details"),
    path('profile/', views.profile, name='profile'),
    
]
