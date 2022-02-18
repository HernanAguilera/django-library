from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple, ClearableFileInput
from .models import Book, Category

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'summary', 'author', 'categories', 'cover']
        widgets = {
                'name': TextInput(attrs={'class': 'form-control'}),
                'summary': Textarea(attrs={'class': 'form-control'}),
                'author': TextInput(attrs={'class': 'form-control'}),
                'categories': SelectMultiple(attrs={'class': 'form-control'}, choices=Category.objects.all()),
                'cover': ClearableFileInput(attrs={'class': 'form-control-file'})
            }
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['description']
        widgets = {
                'description': TextInput(attrs={'class': 'form-control'})
            }