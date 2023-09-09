from django.contrib import admin
from django.urls import path
from poesias.views import home, fepi, movie_detail
from poesias import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('fepi', fepi),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),

    # Extends
    path('page_extends/', views.page_extends),
    path('principal/', views.principal, name='Principal'),
    path('sobre/', views.sobre, name='Sobre'),

    # Tag if
    path('poema_detail/', views.poema_detail),

    # tag for
    path('poema_list/', views.poema_list, name='poema_list'),

    # Passando parâmtros dinâmicamente
    path('poemas/<int:poema_id>/', views.poema_text),
    path('poemas_din/', views.poema_din),

    # Categorias e tratamento e erro
    path('poemas/categorias/<int:category_id>',
         views.category, name='category_id'),

    # Categorias e tratamento  com get_list_or_404
    path('poemas/categorias_404/<int:category_id>',
         views.category_404, name='category_id'),

    # Autores e tratamento de erro
    path('poemas/autor/<int:author_id>',
         views.author, name='author_id'),

]
