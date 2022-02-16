from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    paginate_by = 10
    model = Book
    template_name = 'books/list.html'
