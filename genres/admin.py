from django.contrib import admin
from genres.models import LiteraryGenre

class LiteraryGenderAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)
    search_fields = ("name",)

admin.site.register(LiteraryGenre, LiteraryGenderAdmin)
