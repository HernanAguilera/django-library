from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple, ClearableFileInput
from .models import Book, Author, Category

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'summary', 'author', 'categories', 'cover']
        widgets = {
                'name': TextInput(attrs={'class': 'form-control'}),
                'summary': Textarea(attrs={'class': 'form-control'}),
                'author': Select(attrs={'class': 'form-control'}, choices=Author.objects.all()),
                'categories': SelectMultiple(attrs={'class': 'form-control'}, choices=Category.objects.all()),
                'cover': ClearableFileInput(attrs={'class': 'form-control-file'})
            }