from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple, ClearableFileInput
from .models import Book, Category

def choices_categories():
    try:
        return Category.objects.all() if Category.objects.count()>0 else []
    except Exception:
        return []

class BookForm(ModelForm):
    class Meta:
        choices = choices_categories()
        model = Book
        fields = ['name', 'summary', 'author', 'categories', 'cover']
        widgets = {
                'name': TextInput(attrs={'class': 'form-control'}),
                'summary': Textarea(attrs={'class': 'form-control'}),
                'author': TextInput(attrs={'class': 'form-control'}),
                'categories': SelectMultiple(attrs={'class': 'form-control'}, choices=choices),
                'cover': ClearableFileInput(attrs={'class': 'form-control-file'})
            }
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['description']
        widgets = {
                'description': TextInput(attrs={'class': 'form-control'})
            }