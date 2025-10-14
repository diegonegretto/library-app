from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView
from books.forms import BookModelForm
from books.models import Book
from genres.models import LiteraryGenre
from authors.models import Author
from django.http import HttpResponseRedirect
from django.urls import reverse

#class HomeView(TemplateView):
#    template_name = "index.html"

def home_view(request):
    return HttpResponseRedirect(reverse('books_list', ))
    

class BooksListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"

    def get_queryset(self):
        books = super().get_queryset().order_by("title")
        return books


class NewBookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookModelForm
    template_name = "new_book.html"
    success_url = reverse_lazy("books_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        context["genres"] = LiteraryGenre.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = "book_update.html"

    def get_success_url(self):
        return reverse_lazy("book_detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        context["genres"] = LiteraryGenre.objects.all()
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("books_list")


class UserBooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books_user.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user).order_by("title")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Book.objects.filter(created_by=self.request.user).values("author_id").distinct().count()
        genres = Book.objects.filter(created_by=self.request.user).values("literary_genre_id").distinct().count()
        context["authors"] = authors
        context["genres"] = genres
        return context

