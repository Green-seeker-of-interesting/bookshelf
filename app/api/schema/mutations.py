import graphene
from slugify import slugify

from api.schema.inputs import AuthorInput, GenreInput
from api.schema.types import AuthorType, GenreType

from web_client.models import Author, Genre


class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        author_instance = Author(
            name=input.name, description=input.description, slug=slugify(input.name))
        author_instance.save()
        return CreateAuthor(ok=ok, author=author_instance)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            ok = True
            author_instance.name = input.name
            author_instance.description = input.description
            author_instance.save()
            return UpdateAuthor(ok=ok, author=author_instance)
        return UpdateAuthor(ok=ok, author=None)


class CreateGenre(graphene.Mutation):
    class Arguments:
        input = GenreInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(GenreType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        instance = Genre(
            title=input.title, description=input.description, slug=slugify(input.title))
        instance.save()
        return CreateGenre(ok=ok, author=instance)


class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = GenreInput(required=True)

    ok = graphene.Boolean()
    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        instance = Genre.objects.get(pk=id)
        if instance:
            ok = True
            instance.title = input.title
            instance.description = input.description
            instance.save()
            return UpdateGenre(ok=ok, genre=instance)
        return UpdateGenre(ok=ok, genre=None)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()

    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
