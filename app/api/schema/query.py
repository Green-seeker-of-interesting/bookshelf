import graphene
from graphene_django.types import ObjectType

from core.receive_data import ReceiverData, ModelName

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
            return ReceiverData(ModelName.AUTHOR).get_by_pk(id)
        return None

    def resolve_authors(self, info, **kwargs):
        return ReceiverData(ModelName.AUTHOR).get_all()

    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ReceiverData(ModelName.GENRE).get_by_pk(id)
        return None

    def resolve_genres(self, info, **kwargs):
        return ReceiverData(ModelName.GENRE).get_all()

    def resolve_publisher(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ReceiverData(ModelName.PUBLISHER).get_by_pk(id)
        return None

    def resolve_publishers(self, info, **kwargs):
        return ReceiverData(ModelName.PUBLISHER).get_all()

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ReceiverData(ModelName.BOOK).get_by_pk(id)
        return None

    def resolve_books(self, info, **kwargs):
        return ReceiverData(ModelName.BOOK).get_all()
