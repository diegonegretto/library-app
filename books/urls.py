from books.views import BooksListView, NewBookCreateView, BookDetailView, BookUpdateView, BookDeleteView,  UserBooksListView
from django.urls import path

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('user_books/', UserBooksListView.as_view(), name='user_books'), 
    path('new_book/', NewBookCreateView.as_view(), name='new_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]