from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "literary_genre", "number_page", "publication_year", "synopsis", "photo",)
    search_fields = ("title", "author",)


admin.site.register(Book, BookAdmin)
