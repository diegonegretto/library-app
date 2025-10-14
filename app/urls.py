"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import RegisterView, UserLoginView, UserLogoutView, UserUpdateView, UserPasswordChangeView, UserProfileView, UserDeleteView
from genres.views import NewLiteraryGenreCreateView, LiteraryGenresListView, LiteraryGenreUpdateView, LiteraryGenreDeleteView
from authors.views import  NewAuthorCreateView,  AuthorsListView, AuthorDetailView, AuthorDeleteView, AuthorUpdateView
from books.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', HomeView.as_view(), name='landing'),
    path('', home_view, name='landing'),
    path('books/', include('books.urls')),
    path('authors/', AuthorsListView.as_view(), name='authors_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('new_author/', NewAuthorCreateView.as_view(), name='new_author'),
    path('genres/', LiteraryGenresListView.as_view(), name="genres_list"),
    path('new_genre/', NewLiteraryGenreCreateView.as_view(), name='new_genre'),
    path('genre/<int:pk>/update/', LiteraryGenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:pk>/delete/', LiteraryGenreDeleteView.as_view(), name='genre_delete'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', UserUpdateView.as_view(), name='user_update'),
    path('profile/password/', UserPasswordChangeView.as_view(), name='password_change'),
    path('profile/delete/', UserDeleteView.as_view(), name='user_delete'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
