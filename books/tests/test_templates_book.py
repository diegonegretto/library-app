from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Book, Author, LiteraryGenre


class BooksListViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('books_list'))

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)


class UserBooksListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('user_books')

    def test_user_books_without_login(self):
        """Usuário não autenticado deve ser redirecionado (302)."""
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 302)

    def test_user_books_with_login(self):
        """Usuário autenticado deve ter acesso à página (200)."""
        user = User.objects.create_user(username='tester', password='12345')
        self.client.login(username='tester', password='12345')
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)


class NewBookCreateViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('new_book'))

    def test_302_or_200_response(self):
        # Pode exigir login
        self.assertIn(self.resp.status_code, [200, 302])


class BookDetailViewTest(TestCase):
    def setUp(self):
        # Cria instâncias mínimas para o Book
        self.user = User.objects.create_user(username='tester', password='123')
        self.author = Author.objects.create(name='Autor Teste')
        self.genre = LiteraryGenre.objects.create(name='Ficção')
        self.book = Book.objects.create(
            title='Livro Teste',
            author=self.author,
            literary_genre=self.genre,
            created_by=self.user
        )
        self.resp = self.client.get(reverse('book_detail', args=[self.book.pk]))

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)


class BookUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.author = Author.objects.create(name='Autor Teste')
        self.genre = LiteraryGenre.objects.create(name='Romance')
        self.book = Book.objects.create(
            title='Livro Antigo',
            author=self.author,
            literary_genre=self.genre,
            created_by=self.user
        )
        self.resp = self.client.get(reverse('book_update', args=[self.book.pk]))

    def test_302_or_200_response(self):
        # Pode exigir login
        self.assertIn(self.resp.status_code, [200, 302])


class BookDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='123')
        self.author = Author.objects.create(name='Autor Teste')
        self.genre = LiteraryGenre.objects.create(name='Aventura')
        self.book = Book.objects.create(
            title='Livro Deletar',
            author=self.author,
            literary_genre=self.genre,
            created_by=self.user
        )
        self.resp = self.client.get(reverse('book_delete', args=[self.book.pk]))

    def test_302_or_200_response(self):
        # Pode exigir login
        self.assertIn(self.resp.status_code, [200, 302])
