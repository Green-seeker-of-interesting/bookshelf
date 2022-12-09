import graphene

from api.schema.inputs import AuthorInput, GenreInput, PublishenInput, BookInput
from api.schema.types import AuthorType, GenreType, PublisherType, BookType

from core.receive_data import ModelName, ReceiverData
from core.form_handler import FormHandler


class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        model = FormHandler().add_model_from_form(ModelName.AUTHOR, input)
        return CreateAuthor(ok=ok, author=model)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    ok = graphene.Boolean()
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        model, ok = ReceiverData(
            ModelName.AUTHOR).update_model_by_id(input, id)
        return UpdateAuthor(ok=ok, author=model)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        ok = ReceiverData(ModelName.AUTHOR).delete_model_by_pk(id)
        return DeleteAuthor(ok=ok)


class CreateGenre(graphene.Mutation):
    class Arguments:
        input = GenreInput(required=True)

    ok = graphene.Boolean()
    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        model = FormHandler().add_model_from_form(ModelName.GENRE, input)
        return CreateGenre(ok=ok, genre=model)


class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = GenreInput(required=True)

    ok = graphene.Boolean()
    genre = graphene.Field(GenreType)

    @staticmethod
    def mutate(root, info, id, input=None):
        model, ok = ReceiverData(ModelName.GENRE).update_model_by_id(input, id)
        return UpdateGenre(ok=ok, genre=model)


class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        ok = ReceiverData(ModelName.GENRE).delete_model_by_pk(id)
        return DeleteGenre(ok=ok)


class CreatePublisher(graphene.Mutation):
    class Arguments:
        input = PublishenInput(required=True)

    ok = graphene.Boolean()
    publisher = graphene.Field(PublisherType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        model = FormHandler().add_model_from_form(ModelName.PUBLISHER, input)
        return CreateGenre(ok=ok, publisher=model)


class UpdatePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PublishenInput(required=True)

    ok = graphene.Boolean()
    publisher = graphene.Field(PublisherType)

    @staticmethod
    def mutate(root, info, id, input=None):
        model, ok = ReceiverData(
            ModelName.PUBLISHER).update_model_by_id(input, id)
        return UpdatePublisher(ok=ok, publisher=model)


class DeletePublisher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        ok = ReceiverData(ModelName.PUBLISHER).delete_model_by_pk(id)
        return DeletePublisher(ok=ok)


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    ok = graphene.Boolean()
    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        print(input['author'][0].id)
        # model = FormHandler().add_model_from_form(ModelName.PUBLISHER, input)
        # return CreateGenre(ok=ok, publisher=model)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()

    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()

    create_publisher = CreatePublisher.Field()
    update_publisher = UpdatePublisher.Field()
    delete_publisher = DeletePublisher.Field()

    create_book = CreateBook.Field()
