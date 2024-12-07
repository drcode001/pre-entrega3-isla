from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name='blog'),
    path("home/", views.home, name='home'),  # Página principal
    path('add/', views.add_data, name='add_data'),  # Añadir datos
    path('search/', views.search_books, name='search_books'),  # Buscar libros
]
