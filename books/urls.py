from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BooksListView.as_view(), name='books_list'),
    path('user_books/', views.UserBooksListView.as_view(), name='user_books'), 
    path('new_book/', views.NewBookCreateView.as_view(), name='new_book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]