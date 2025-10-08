from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from authors.forms import AuthorModelForm 
from authors.models import Author
from books.models import Book


class AuthorsListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = "authors.html"
    context_object_name = "authors"

    def get_queryset(self):
        authors = super().get_queryset().order_by("name")
        return authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nationalities = Author.objects.values("nationality").distinct().count()
        books = Book.objects.all().count()
        context["nationalities"] = nationalities
        context["books"] = books
        return context
    

class NewAuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorModelForm
    template_name = "new_author.html"
    success_url = reverse_lazy("authors_list")


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = "author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs.get("pk")        
        context["books"] = Book.objects.filter(author_id = author_id).count()   
        return context


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorModelForm
    template_name = "author_update.html"

    def get_success_url(self):
        return reverse_lazy("author_detail", kwargs={"pk": self.object.pk})
    

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = "author_delete.html"
    success_url = reverse_lazy("authors_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"❌ Não é possível excluir o autor '{self.object.name}' porque ele possui livros cadastrados."
            )
            return render(request, self.template_name, {"object": self.object})
