from django.shortcuts import render, redirect
from .models import Author, Book, Genre
from .forms import AuthorForm, BookForm, GenreForm, SearchForm

def home(request):
    return render(request, 'biblioteca/gestion/templates/home.html')

def add_data(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, prefix='author')
        genre_form = GenreForm(request.POST, prefix='genre')
        book_form = BookForm(request.POST, prefix='book')
        if author_form.is_valid() and genre_form.is_valid() and book_form.is_valid():
            author_form.save()
            genre_form.save()
            book_form.save()
            return redirect('home')
    else:
        author_form = AuthorForm(prefix='author')
        genre_form = GenreForm(prefix='genre')
        book_form = BookForm(prefix='book')

    return render(request, 'gestion/add_data.html', {
        'author_form': author_form,
        'genre_form': genre_form,
        'book_form': book_form,
    })

def search_books(request):
    results = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
    else:
        form = SearchForm()

    return render(request, 'gestion/search_books.html', {'form': form, 'results': results})

# Create your views here.
