from django.contrib import admin

from .models import Author, Genre, Publisher, Book


@admin.register(Author)
class AuthorRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Genre)
class GenreRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

@admin.register(Publisher)
class PublisherRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

@admin.register(Book)
class BookRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}



