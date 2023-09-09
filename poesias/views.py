from .models import Movie, Book
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render
from poesias.utils.poesias.factory import make_poetry


def home(request):
    return render(request, 'home.html', context={'name': 'Prof. Gabriel'})


def fepi(request):
    return render(request, 'fepi.html', context={'name': 'Prof. Gabriel'})


def page_extends(request):
    return render(request, 'page_extends.html')


def principal(request):
    return render(request, "principal.html")


def sobre(request):
    return render(request, "sobre.html")


def movie_detail(request, movie_id):
    # Pega o filme com base no ID fornecido. Se não existir, retorna um erro 404.
    print("MOVIEEEEE", movie_id)
    movie = get_object_or_404(Movie, id=movie_id)
    # Renderiza o template 'movie_detail.html' e passa o objeto do filme para ele.
    return render(request, 'movie_detail.html', {'movie': movie})


def poema_text(request, poema_id):
    return render(request, 'partial/poema_detail.html')


# Query set para buscar a categoria de um livro pelo ID do livro com get_list_or_404
def category(request, category_id):
    books = Book.objects.filter(
        categories__id=category_id,
    )

    if not books:
        raise Http404("Not found ")

    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books.first().categories.all()[0]}'
    })

# Query set para buscar a categoria de um livro pelo ID do livro


def category_404(request, category_id):
    books = get_list_or_404(
        Book.objects.filter
        (
            categories__id=category_id,
        )
    )
    print("Books: ", books)
    print("Books: ", books[0])
    print("Books: ", books[0].categories.all()[0])
    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books[0].categories.all()[0]}'
    })

# Query set para buscar o autor de um livro pelo ID do livro


def author(request, author_id):
    books = Book.objects.filter(
        author__id=author_id,
    )

    if not books:
        raise Http404("Not found ")

    return render(request, 'author.html', context={
        'books': books,
        'title': f'Autor: {books.first().author.name}'
    })

# Tag If


def poema_detail(request):
    poetry = make_poetry()
    return render(request, 'poema_detail.html', {'poetry': poetry})

# Tag for


def poema_list(request):
    poesias = [make_poetry() for _ in range(5)]
    return render(request, 'poema_list.html', {'poesias': poesias})


def poema_din(request):
    return render(request, 'partial/poema_din.html', context={
        'poesias': [make_poetry() for _ in range(3)]
    })


def my_view(request):
    return HttpResponse("Uma teste string de resposta")


def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")


def root_view(request):
    return HttpResponse("Estamos na Raiz 2. Porta 8000")
