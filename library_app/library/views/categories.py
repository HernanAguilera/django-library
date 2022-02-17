from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from ..models import Category
from ..forms import CategoryForm

SUCCESS_URL = reverse_lazy('category_list')

class CategoryListView(ListView):
    paginate_by = 10
    model = Category
    template_name = 'categories/list.html'
    
class CategoryCrateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/create.html'
    success_url = SUCCESS_URL

class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/edit.html'
    success_url = SUCCESS_URL

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/delete.html"
    success_url = SUCCESS_URL
