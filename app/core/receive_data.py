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

    def __init__(self, model_name: ModelName) -> None:
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

    # TODO зачем тут request переделать на более внятный стиль
    def get_with_terms(self, request) -> QuerySet:
        kit: QuerySet = self.get_all()
        ordering = request.GET.get('ord', None)
        if ordering:
            kit = kit.order_by(ordering)
        return kit

    def get_with_filters(self, request):
        kit = self.get_all()
        genre = request.POST['genre']
        if genre:
            kit = kit.filter(genre=genre)
        publisher = request.POST['publisher']
        if publisher:
            kit = kit.filter(publisher=publisher)
        author = request.POST['author']
        if author:
            kit = kit.filter(author=author)
        return kit

    def get_by_slug(self, slug: str):
        return get_object_or_404(self.model, slug=slug)

    def get_by_pk(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def add_model(self, model):
        if self.model_name == ModelName.BOOK:
            model.slug = slugify(model.title)
        else:
            model.slug = slugify(model.name)
        model.save()

    def update_model_by_slug(self, cleaned_data, slug):
        if self.model_name == ModelName.BOOK:
            self._update_book(cleaned_data, slug)
        else:
            self._update_generic(cleaned_data, slug)

    def _update_generic(self, cleaned_data, slug):
        model = self.get_by_slug(slug)
        model.name = cleaned_data['name']
        model.description = cleaned_data['description']
        model.save()

    def _update_book(self, cleaned_data, slug):
        model = self.get_by_slug(slug)
        model.title = cleaned_data['title']
        model.description = cleaned_data['description']
        model.genre = ReceiverData(ModelName.GENRE).get_by_pk(
            cleaned_data['genre'][0])
        model.publisher = ReceiverData(ModelName.PUBLISHER).get_by_pk(
            cleaned_data['publisher'][0])
        for author_pk in cleaned_data.getlist('author'):
            model.author.add(ReceiverData(
                ModelName.AUTHOR).get_by_pk(author_pk))
        model.save()

    def delete_model_by_slug(self, slug: str):
        model = self.get_by_slug(slug)
        model.delete()

    def delete_model_by_pk(self, pk):
        model = self.get_by_pk(pk)
        model.delete()
        return True

    def update_model_by_id(self, cleaned_data, id):
        if self.model_name == ModelName.BOOK:
            return self._update_book_id(cleaned_data, id)
        else:
            return self._update_generic_id(cleaned_data, id)

    def _update_generic_id(self, cleaned_data, id):
        model = self.get_by_pk(id)
        model.name = cleaned_data['name']
        model.description = cleaned_data['description']
        model.save()
        return model, True

    def _update_book_id(self, cleaned_data, id):
        model = self.get_by_pk(id)
        model.title = cleaned_data['title']
        model.description = cleaned_data['description']
        model.genre = ReceiverData(ModelName.GENRE).get_by_pk(
            cleaned_data['genre'][0])
        model.publisher = ReceiverData(ModelName.PUBLISHER).get_by_pk(
            cleaned_data['publisher'][0])
        for author_pk in cleaned_data.getlist('author'):
            model.author.add(ReceiverData(
                ModelName.AUTHOR).get_by_pk(author_pk))
        model.save()
        return model, True
