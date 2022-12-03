import graphene
from graphene_django.types import ObjectType

from web_client.models import Author, Book, Genre, Publisher

from api.schema.types import AuthorType, BookType, GenreType, PublisherType


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    genre = graphene.Field(GenreType, id=graphene.Int())
    genres = graphene.List(GenreType)

    publisher = graphene.Field(PublisherType, id=graphene.Int())
    publishers = graphene.List(PublisherType)

    book = graphene.Field(BookType, id=graphene.Int())
    books = graphene.List(BookType)

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Author.objects.get(pk=id)
        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Genre.objects.get(pk=id)
        return None

    def resolve_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_publisher(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Publisher.objects.get(pk=id)
        return None

    def resolve_publishers(self, info, **kwargs):
        return Publisher.objects.all()

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Book.objects.get(pk=id)
        return None

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()
