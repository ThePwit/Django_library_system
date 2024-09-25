from django.urls import path
from . import views
   
urlpatterns = [
    path("book_details/<int:pk>/", views.BookDetailView.as_view(), name="book_details"),
    path('', views.home, name='home'),
    path('book_list/create/', views.AddBookView, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    #path("book_details2/<int:pk>/", views.BookDetails.as_view(), name="book_details"),
]
