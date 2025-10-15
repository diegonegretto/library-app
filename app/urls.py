from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('library/', include('books.urls')),
    path('library/', include('authors.urls')),
    path('library/', include('genres.urls')),
    path('library/', include('accounts.urls')),  
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
