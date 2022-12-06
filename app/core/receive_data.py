from enum import IntEnum

from django.db.models.query import QuerySet

from web_client.models import Author, Genre, Publisher, Book

class ModelName(IntEnum):
    AUTHOR = 1
    GENRE = 2
    PUBLISHER = 3
    BOOK = 4


class ReceiverData:

    def __init__(self, model_name:ModelName) -> None:
        if model_name == ModelName.AUTHOR:
            self.model = Author
        elif model_name == ModelName.GENRE:
            self.model = Genre
        elif model_name == ModelName.PUBLISHER:
            self.model = Publisher
        elif model_name == ModelName.BOOK:
            self.model = Book

    def get_all(self):
        return self.model.objects.all()

    def get_with_terms(self, request): # TODO зачем тут request переделать на более внятный стиль
        kit:QuerySet = self.get_all()
        ordering = request.GET.get('ord')
        if ordering:
            kit = kit.order_by(ordering)
        return kit

        
        




