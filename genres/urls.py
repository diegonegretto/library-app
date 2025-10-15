from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.LiteraryGenresListView.as_view(), name="genres_list"),
    path('new_genre/', views.NewLiteraryGenreCreateView.as_view(), name='new_genre'),
    path('genre/<int:pk>/update/', views.LiteraryGenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:pk>/delete/', views.LiteraryGenreDeleteView.as_view(), name='genre_delete'),
]