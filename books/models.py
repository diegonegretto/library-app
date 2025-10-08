from django.contrib.auth.models import User
from django.db import models
from genres.models import LiteraryGenre
from authors.models import Author
   

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="book_author")
    literary_genre = models.ForeignKey(LiteraryGenre, on_delete=models.PROTECT, related_name="book_genre")
    number_page = models.IntegerField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="books/", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_user")

    def __str__(self):
        return self.title
