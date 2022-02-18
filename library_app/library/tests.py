from io import BytesIO
import os
import random
from unicodedata import category
from django.urls import reverse
from django.test import TestCase

from .models import Book, Category
from faker import Faker

fake = Faker()
    

def create_category():
    category = Category(**{
        'description': fake.text(max_nb_chars=20)
    })
    category.save()
    return category

def create_books(n: int):
    books = []
    for _ in range(n):
        book = Book(**{
            'name': fake.text(max_nb_chars=20),
            'summary': fake.text(),
            'cover': fake.file_path(),
            'author': '{} {}'.format(fake.first_name(), fake.last_name())
        })
        book.save()
        book.categories.add(create_category())
        books.append(book)
                
    return books

class BookViewsTest(TestCase):
    
    def test_list_of_books(self):
        books = create_books(random.randint(1, 100))
        # print(book.id, book.cover, book.categories.all())
        response = self.client.get(reverse('book_list'))
        # print(response.context['object_list'].count())
        self.assertEqual(response.context['object_list'].count(), len(books) if len(books)<=12 else 12)
        
        
    def test_create_book_with_correct_data(self):
        category = create_category()
        path_to_this_file = os.path.dirname(os.path.realpath(__file__))
        cover = open(os.path.join(path_to_this_file, 'cat.jpg'), 'rb')
        
        data = {
            'name': fake.text(max_nb_chars=20),
            'summary': fake.text(),
            'cover': cover,
            'author': '{} {}'.format(fake.first_name(), fake.last_name()),
            'categories': [category.id],
        }
        response = self.client.post(reverse('book_create'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].count(), 1)
        cover.close()
        
    def test_retrieve_individual_books(self):
        books = create_books(1)
        # print(book.id, book.cover, book.categories.all())
        response = self.client.get(reverse('book_detail', args=[books[0].id]))
        # print(response.context['object_list'].count())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].id, books[0].id)
        
        
    # def test_update_book_with_correct_data(self):
    #     book =create_books(1)
    #     category = create_category()
    #     path_to_this_file = os.path.dirname(os.path.realpath(__file__))
    #     cover = open(os.path.join(path_to_this_file, 'cat.jpg'), 'rb')
        
    #     data = {
    #         'name': fake.text(max_nb_chars=20),
    #         'summary': fake.text(),
    #         'cover': cover,
    #         'author': '{} {}'.format(fake.first_name(), fake.last_name()),
    #         'categories': [category.id],
    #     }
    #     print('url', reverse('book_edit', args=[book[0].id]))
    #     response = self.client.post(reverse('book_edit', args=[book[0].id]), data, follow=True)
    #     print(response.content)
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertEqual(response.context['object_list'].count(), 1)
    
    def test_delete_existent_book(self):
        book =create_books(1)
        
        print('url', reverse('book_delete', args=[book[0].id]))
        response = self.client.post(reverse('book_delete', args=[book[0].id]), follow=True)
        print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 0)