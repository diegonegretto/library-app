from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from genres.forms import LiteraryGenreModelForm
from genres.models import LiteraryGenre


class LiteraryGenresListView(LoginRequiredMixin, ListView):
    model = LiteraryGenre
    template_name = "genres.html"
    context_object_name = "genres"

    def get_queryset(self):
        genres = super().get_queryset().order_by("name")
        return genres


class NewLiteraryGenreCreateView(LoginRequiredMixin, CreateView):
    model = LiteraryGenre
    form_class = LiteraryGenreModelForm
    template_name = "new_genre.html"
    success_url = reverse_lazy("genres_list")


class LiteraryGenreUpdateView(LoginRequiredMixin, UpdateView):
    model = LiteraryGenre
    form_class = LiteraryGenreModelForm
    template_name = "genre_update.html"
    success_url = reverse_lazy("genres_list")
   

class LiteraryGenreDeleteView(LoginRequiredMixin, DeleteView):
    model = LiteraryGenre
    template_name = "genre_delete.html"
    success_url = reverse_lazy("genres_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"❌ Não é possível excluir o gênero '{self.object.name}' porque ele está vinculado a livros cadastrados."
            )
            return render(request, self.template_name, {"object": self.object})
