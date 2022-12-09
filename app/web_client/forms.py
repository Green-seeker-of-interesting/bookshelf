from django import forms

from web_client.models import Author, Genre, Publisher, Book
from core.receive_data import ReceiverData, ModelName


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


class FilterForms(forms.Form):
    genre = forms.ModelChoiceField(queryset=ReceiverData(
        model_name=ModelName.GENRE).get_all(), required=False)
    publisher = forms.ModelChoiceField(queryset=ReceiverData(
        model_name=ModelName.PUBLISHER).get_all(), required=False)
    author = forms.ModelChoiceField(queryset=ReceiverData(
        model_name=ModelName.AUTHOR).get_all(), required=False)
