from graphene_django.types import DjangoObjectType

from web_client.models import Author, Genre, Publisher, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher


class BookType(DjangoObjectType):
    class Meta:
        model = Book
