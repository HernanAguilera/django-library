from unicodedata import category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from ..models import Book, Category
from ..forms import BookForm

SUCCESS_URL = reverse_lazy('book_list')

class BookListView(ListView):
    paginate_by = 12
    model = Book
    template_name = 'books/list.html'
    
    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.GET.get("category"):
            category_id = self.request.GET.get("category")
            queryset = Book.objects.filter(categories__id=category_id)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        try:
            context['category_searched'] = int(self.request.GET.get("category", ""))
        except ValueError:
            pass
        return context
    
class BookDetailView(DetailView):
    model = Book
    template_name = "books/detail.html"

    
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
