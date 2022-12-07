from enum import IntEnum

from slugify import slugify
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404


from web_client.models import Author, Genre, Publisher, Book

class ModelName(IntEnum):
    AUTHOR = 1
    GENRE = 2
    PUBLISHER = 3
    BOOK = 4


class ReceiverData:

    def __init__(self, model_name:ModelName) -> None:
        self.model_name = model_name

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

    def get_by_slug(self, slug:str):
        return get_object_or_404(self.model, slug=slug)

    def add_model(self, model):
        if self.model_name == ModelName.BOOK:
            model.slug = slugify(model.title)
        else:
            model.slug = slugify(model.name)
            model.save()

    def update_model(self, cleaned_data, slug):
        model = self.get_by_slug(slug)
        model.name = cleaned_data['name']
        model.description = cleaned_data['description']
        model.save()

    def delete_model(self, slug:str):
        model = self.get_by_slug(slug)
        model.delete()


        
        




