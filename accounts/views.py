from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from books.models import Book


class RegisterView(CreateView):    
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"   
    redirect_authenticated_user = True

    def get_success_url(self):
        # Força sempre ir para books, ignorando qualquer 'next'
        return reverse_lazy("books_list")

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("books_list")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user_profile.html"
    context_object_name = "user_profile"
    
    def get_object(self):
        # SEMPRE retorna o usuário logado, ignorando qualquer pk na URL
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(created_by=self.request.user).count()   
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = "user_update.html"   

    def get_object(self):
        # SEMPRE retorna o usuário logado, ignorando qualquer pk na URL
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("user_profile")
    

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "password_change.html"     

    def get_success_url(self):
        return reverse_lazy("user_profile")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "user_delete_confirm.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Sua conta foi deletada com sucesso.")
        return super().delete(request, *args, **kwargs)