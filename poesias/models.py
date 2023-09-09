# models.py

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    overview = models.TextField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    poster_path = models.ImageField(upload_to='posters/')
    trailer_link = models.URLField(blank=True, null=True)


# Definindo um modelo de Categoria
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Definindo um modelo de Autor


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Definindo um modelo de Livro com relacionamento ManyToMany com Categoria e Autor


class Book(models.Model):
    title = models.CharField(max_length=200)
    # Relacionamento com Autor
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    # Relacionamento ManyToMany com Categoria
    categories = models.ManyToManyField(Category)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    # Campo para upload de imagem
    cover = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title
