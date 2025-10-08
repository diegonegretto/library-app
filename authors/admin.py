from django.contrib import admin
from authors.models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date", "nationality", "biography", "photo",)
    search_fields = ("name",)


admin.site.register(Author, AuthorAdmin)
