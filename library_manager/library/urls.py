from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookListAPI, basename='booklist')
router.register(r'authors', views.AuthorAPI, basename='authorlist')
   
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.AddBookView.as_view(), name='add_book'),
    path("book_details/<int:pk>/", views.BookDetailView.as_view(), name="book_details"),
    path('profile/', views.profile, name='profile'), 
    path('api/', include(router.urls)),
]

