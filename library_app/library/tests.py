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
        
        response = self.client.get(reverse('book_list'))
        
        self.assertEqual(response.context['object_list'].count(), len(books) if len(books)<=12 else 12)
        
        
        
    def test_create_book_with_correct_data(self):
        category = create_category()
        path_to_this_file = os.path.dirname(os.path.realpath(__file__))
        cover = open(os.path.join(path_to_this_file, 'test_imgs','cat.jpg'), 'rb')
        
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
        
        
        
    def test_create_book_with_wrong_data(self):
        for data in self.get_wrong_data_to_create():
            response = self.client.post(reverse('book_create'), data, follow=True)
            self.assertTrue('form' in response.context)
            self.assertContains(response, 'This field is required')
        


    def test_retrieve_individual_book(self):
        books = create_books(1)
        
        response = self.client.get(reverse('book_detail', args=[books[0].id]))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].id, books[0].id)
    
    
    
    def test_trying_to_retrieve_inexistent_book(self):
        
        response = self.client.get(reverse('book_detail', args=[ random.randint(0, 100) ]))
        
        self.assertEqual(response.status_code, 404)
    
    
    def test_update_a_book_with_correct_data(self):
        book =create_books(1)
        category = create_category()
        path_to_this_file = os.path.dirname(os.path.realpath(__file__))
        cover = open(os.path.join(path_to_this_file, 'test_imgs','cat.jpg'), 'rb')
        
        data = {
            'name': fake.text(max_nb_chars=20),
            'summary': fake.text(),
            'cover': cover,
            'author': '{} {}'.format(fake.first_name(), fake.last_name()),
            'categories': [category.id],
        }
        response = self.client.post(reverse('book_edit', args=[book[0].id]), data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'][0].name, data['name'])
    
    
    def test_trying_to_update_inexistent_book(self):
        response = self.client.get(reverse('book_edit', args=[ random.randint(0, 100) ]))
        
        self.assertEqual(response.status_code, 404)
    
    
    def test_update_a_book_with_wrong_data(self):
        book =create_books(1)
        for data in self.get_wrong_data_to_update():
            response = self.client.post(reverse('book_edit', args=[book[0].id]), data, follow=True)
            self.assertTrue('form' in response.context)
            self.assertContains(response, 'This field is required')
            self.assertEqual(Book.objects.count(), 1)
    
    
    def test_deleting_an_existent_book(self):
        book =create_books(1)
        
        response = self.client.post(reverse('book_delete', args=[book[0].id]), follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 0)
        
    
    def test_trying_to_delete_inexistent_book(self):
        response = self.client.get(reverse('book_delete', args=[ random.randint(0, 100) ]))
        
        self.assertEqual(response.status_code, 404)
        
    
    def get_wrong_data_to_create(self):
        path_to_this_file = os.path.dirname(os.path.realpath(__file__))
        cover = open(os.path.join(path_to_this_file, 'test_imgs','cat.jpg'), 'rb')
        category = create_category()
        name = fake.text(max_nb_chars=20)
        summary = fake.text()
        author = '{} {}'.format(fake.first_name(), fake.last_name())
        categories = [category.id]
        return [
            {
                'summary': summary,
                'cover': cover,
                'author': author,
                'categories': categories,
            },
            {
                'name': name,
                'cover': cover,
                'author': author,
                'categories': categories,
            },
            {
                'name': name,
                'summary': summary,
                'author': author,
                'categories': categories,
            },
            {
                'name': name,
                'summary': summary,
                'cover': cover,
                'categories': categories,
            },
            {
                'name': name,
                'summary': summary,
                'cover': cover,
                'author': author,
            },
        ]
        
        
    def get_wrong_data_to_update(self):
        path_to_this_file = os.path.dirname(os.path.realpath(__file__))
        cover = open(os.path.join(path_to_this_file, 'test_imgs','cat.jpg'), 'rb')
        category = create_category()
        name = fake.text(max_nb_chars=20)
        summary = fake.text()
        author = '{} {}'.format(fake.first_name(), fake.last_name())
        categories = [category.id]
        return [
            {
                'summary': summary,
                'cover': cover,
                'author': author,
                'categories': categories,
            },
            {
                'name': name,
                'cover': cover,
                'author': author,
                'categories': categories,
            },
            {
                'name': name,
                'summary': summary,
                'cover': cover,
                'categories': categories,
            },
            {
                'name': name,
                'summary': summary,
                'cover': cover,
                'author': author,
            },
        ]