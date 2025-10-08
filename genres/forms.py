from django import forms
from genres.models import LiteraryGenre


class LiteraryGenreModelForm(forms.ModelForm):
    class Meta:
        model = LiteraryGenre
        fields = "__all__"