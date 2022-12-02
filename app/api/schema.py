import graphene
from slugify import slugify

from graphene_django.types import DjangoObjectType, ObjectType

from web_client.models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Author.objects.get(pk=id)
        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


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


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
