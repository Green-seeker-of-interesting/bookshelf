from django.http import QueryDict
from web_client.models import Author, Genre, Publisher, Book

from core.receive_data import ModelName, ReceiverData


class FormHandler:

    def add_model_from_form(self, model_name: ModelName, cleaned_data: QueryDict):
        if model_name == ModelName.AUTHOR:
            return self._add_author(cleaned_data)
        elif model_name == ModelName.GENRE:
            return self._add_genre(cleaned_data)
        elif model_name == ModelName.PUBLISHER:
            return self._add_publisher(cleaned_data)
        elif model_name == ModelName.BOOK:
            return self._add_book(cleaned_data)

    def _add_author(self, cleaned_data: QueryDict):
        print(cleaned_data)
        author = Author(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
        )
        ReceiverData(model_name=ModelName.AUTHOR).add_model(author)
        return author

    def _add_genre(self, cleaned_data: QueryDict):
        model = Genre(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
        )
        ReceiverData(model_name=ModelName.GENRE).add_model(model=model)
        return model

    def _add_publisher(self, cleaned_data: QueryDict):
        model = Publisher(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
        )
        ReceiverData(model_name=ModelName.PUBLISHER).add_model(model=model)
        return model

    def _add_book(self, cleaned_data: QueryDict):
        model = Book(
            title=cleaned_data['title'],
            description=cleaned_data['description'],
            genre=ReceiverData(ModelName.GENRE).get_by_pk(
                cleaned_data['genre'][0]),
            publisher=ReceiverData(ModelName.PUBLISHER).get_by_pk(
                cleaned_data['publisher'][0]),
        )
        ReceiverData(model_name=ModelName.BOOK).add_model(model=model)

        for author_pk in cleaned_data.getlist('author'):
            model.author.add(ReceiverData(
                ModelName.AUTHOR).get_by_pk(author_pk))

        ReceiverData(model_name=ModelName.BOOK).add_model(model=model)

    def update_model_by_slug(self, model_name: ModelName, cleaned_data: QueryDict, slug: str):
        return ReceiverData(model_name=model_name).update_model_by_slug(
            cleaned_data=cleaned_data, slug=slug)
