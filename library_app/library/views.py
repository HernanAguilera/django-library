from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Book
from .forms import BookForm

SUCCESS_URL = reverse_lazy('book_list')

class BookListView(ListView):
    paginate_by = 10
    model = Book
    template_name = 'books/list.html'
    
class BookCrateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = SUCCESS_URL

class BookEditView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/edit.html'
    success_url = SUCCESS_URL
    
    def form_valid(self, form):
        Book.objects.get(pk=self.kwargs['pk']).cover.delete(save=True)
        return super().form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/delete.html"
    success_url = SUCCESS_URL
    
    def form_valid(self, form):
        Book.objects.get(pk=self.kwargs['pk']).cover.delete(save=True)
        return super().form_valid(form)
