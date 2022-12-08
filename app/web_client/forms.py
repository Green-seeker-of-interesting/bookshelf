from django import forms

from web_client.models import Author, Genre, Publisher, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'description', 'is_alive')


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'description')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')
