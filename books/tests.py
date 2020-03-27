from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import Book, Review


class BookTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = 'reviewuser',
            email = 'reviewuser@gmail.com',
            password = 'testpass123'
        )

        self.book = Book.objects.create(
            title = 'Negeri 5 Menara',
            author = 'Ahmad Fuadi',
            price = '67.000',
        )

        self.review = Review.objects.create (
            book = self.book,
            author = self.user,
            review = 'Buku ini terbaik!'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Negeri 5 Menara')
        self.assertEqual(f'{self.book.author}', 'Ahmad Fuadi')
        self.assertEqual(f'{self.book.price}', '67.000')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Negeri 5 Menara')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Negeri 5 Menara')
        self.assertContains(response, 'Buku ini terbaik!')
        self.assertTemplateUsed(response, 'books/book_detail.html')