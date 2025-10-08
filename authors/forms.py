from django import forms
from authors.models import Author


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"