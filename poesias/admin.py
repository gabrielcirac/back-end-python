from django.contrib import admin
from .models import Category, Author, Book
from django.utils.html import mark_safe
''''
O @admin.register(ModelName) é um decorador em Python que registra o modelo 
(no exemplo, Category e Author) no site administrativo do Django. 
É uma forma mais concisa e moderna de registrar modelos no Django Admin, comparada ao método tradicional.'''


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date',)
    list_filter = ('author', 'categories', 'published_date',)
    search_fields = ('title', 'author__name', 'categories__name',)
    readonly_fields = ('cover_preview',)

    def cover_preview(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" width="100" />')

