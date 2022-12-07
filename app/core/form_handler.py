from django.http import QueryDict
from web_client.models import Author, Genre, Publisher, Book

from core.receive_data import ModelName, ReceiverData


class FormHandler:

    def add_model_from_form(self, model_name: ModelName, cleaned_data: QueryDict):
        if model_name == ModelName.AUTHOR:
            return self._add_author(cleaned_data)

    def _add_author(self, cleaned_data: QueryDict) -> bool:
        author = Author(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
        )
        ReceiverData(model_name=ModelName.AUTHOR).add_model(author)

    def update_model(self, model_name: ModelName, cleaned_data: QueryDict, slug: str):
        if model_name == ModelName.AUTHOR:
            return self._update_author(cleaned_data, slug)

    def _update_author(self, cleaned_data: QueryDict, slug: str) -> bool:
        ReceiverData(model_name=ModelName.AUTHOR).update_model(
            cleaned_data=cleaned_data, slug=slug)



