from django import forms

from web_client.models import Author, Genre, Publisher, Book



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'description', 'is_alive')