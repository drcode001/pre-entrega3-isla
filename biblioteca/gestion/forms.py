from django import forms
from .models import Author, Book, Genre

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, label="Buscar libro")
