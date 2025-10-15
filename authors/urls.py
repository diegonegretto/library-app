from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.AuthorsListView.as_view(), name='authors_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('new_author/', views.NewAuthorCreateView.as_view(), name='new_author'),
]