from api.schema.types import BookType
from core.receive_data import ModelName, ReceiverData
from web_client.models import Book


class ApiHendler:

    def add_model(self, model_name: ModelName, cleaned_data: BookType):
        if model_name == ModelName.BOOK:
            return self._add_book(cleaned_data)

    def _add_book(self, cleaned_data: BookType):
        model = Book(
            title=cleaned_data['title'],
            description=cleaned_data['description'],
            genre=ReceiverData(ModelName.GENRE).get_by_pk(
                cleaned_data['genre'].id),
            publisher=ReceiverData(ModelName.PUBLISHER).get_by_pk(
                cleaned_data['publisher'].id),
        )
        ReceiverData(model_name=ModelName.BOOK).add_model(model=model)

        for author_pk in cleaned_data['author']:
            model.author.add(ReceiverData(
                ModelName.AUTHOR).get_by_pk(author_pk.id))

        ReceiverData(model_name=ModelName.BOOK).add_model(model=model)
        return model, True

    def update_model(self, model_name: ModelName, id: int, cleaned_data: BookType):
        if model_name == ModelName.BOOK:
            return self._update_book(id, cleaned_data)

    def _update_book(self, id: int, cleaned_data: BookType):
        model:Book = ReceiverData(ModelName.BOOK).get_by_pk(id)
        model.title = cleaned_data['title']
        model.description = cleaned_data['description']
        model.genre = ReceiverData(ModelName.GENRE).get_by_pk(
            cleaned_data['genre'].id)
        model.publisher = ReceiverData(ModelName.PUBLISHER).get_by_pk(
            cleaned_data['publisher'].id)
        for author_pk in cleaned_data['author']:
            model.author.add(ReceiverData(
                ModelName.AUTHOR).get_by_pk(author_pk.id))
        model.save()
        return model, True
