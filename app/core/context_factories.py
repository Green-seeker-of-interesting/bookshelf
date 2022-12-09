from enum import IntEnum


from core.receive_data import ReceiverData, ModelName
from web_client.forms import AuthorForm, GenreForm, PublisherForm, BookForm, FilterForms


class HendlerName(IntEnum):
    INDEX = 1

    AUTHOR_FORM = 2
    AUTHOR_LIST_TO_EDIT = 3
    AUTHOR_EDIT = 4

    GENRE_FORM = 5
    GENRE_LIST_TO_EDIT = 6
    GENRE_EDIT = 7

    PUBLISHER_FORM = 8
    PUBLISHER_LIST_TO_EDIT = 9
    PUBLISHER_EDIT = 10

    BOOK_FORM = 11
    BOOK_LIST_TO_EDIT = 12
    BOOK_EDIT = 13

    FILTER = 14


SORT_OPTION = [
        {"href": '?ord=title',
        "title": "Сортировка по названию"},
        {"href": '?ord=description',
        "title": "Сортировка по описанию"},
        {"href": '?ord=genre',
        "title": "Сортировка по жанру"},
        {"href": '?ord=publisher',
        "title": "Сортировка по издательству"},
        {"href": '?ord=publication_date',
        "title": "Сортировка по дате"},
    ]

class ContextFactory:

    def get_context(self, hendler_name: HendlerName, request=None):
        if hendler_name == HendlerName.INDEX:
            return self.index_context(request)
        elif hendler_name == HendlerName.AUTHOR_FORM:
            return self.author_form_context(request)
        elif hendler_name == HendlerName.AUTHOR_LIST_TO_EDIT:
            return self.author_list_to_edit(request)
        elif hendler_name == HendlerName.AUTHOR_EDIT:
            return self.author_form_context(request)
        elif hendler_name == HendlerName.GENRE_FORM:
            return self.genre_form_context(request)
        elif hendler_name == HendlerName.GENRE_LIST_TO_EDIT:
            return self.genre_list_to_edit(request)
        elif hendler_name == HendlerName.GENRE_EDIT:
            return self.genre_form_context(request)
        elif hendler_name == HendlerName.PUBLISHER_FORM:
            return self.publisher_form_context(request)
        elif hendler_name == HendlerName.PUBLISHER_LIST_TO_EDIT:
            return self.publisher_list_to_edit(request)
        elif hendler_name == HendlerName.PUBLISHER_EDIT:
            return self.publisher_form_context(request)
        elif hendler_name == HendlerName.BOOK_FORM:
            return self.book_form_context(request)
        elif hendler_name == HendlerName.BOOK_LIST_TO_EDIT:
            return self.book_list_to_edit(request)
        elif hendler_name == HendlerName.BOOK_EDIT:
            return self.book_form_context(request)
        elif hendler_name == HendlerName.FILTER:
            return self.filter_context(request)

    def index_context(self, request) -> dict:

        return {
            "books": ReceiverData(ModelName.BOOK).get_with_terms(request),
            "sort_options": SORT_OPTION,
            "form" : FilterForms(),
            "filter" : True,
        }

    def author_form_context(self, request) -> dict:
        if request:
            author = ReceiverData(ModelName.AUTHOR).get_by_slug(request.slug)
            author_form = AuthorForm(instance=author)
        else:
            author_form = AuthorForm()
        return {
            "form": author_form,
            "title": "Авторы",
            "name": "ФИО"
        }

    def author_list_to_edit(self, request) -> dict:
        models = ReceiverData(model_name=ModelName.AUTHOR).get_all()
        url_interspersed = "author"
        title = "Автор"
        return {
            "models": models,
            "url_interspersed": url_interspersed,
            "title": title,
        }

    def genre_form_context(self, request) -> dict:
        if request:
            model = ReceiverData(ModelName.GENRE).get_by_slug(request.slug)
            form = GenreForm(instance=model)
        else:
            form = GenreForm()
        return {
            "form": form,
            "title": "Жанр",
            "name": "Название"
        }

    def genre_list_to_edit(self, request) -> dict:
        models = ReceiverData(model_name=ModelName.GENRE).get_all()
        url_interspersed = "genre"
        title = "Жанры"
        return {
            "models": models,
            "url_interspersed": url_interspersed,
            "title": title,
        }

    def publisher_form_context(self, request) -> dict:
        if request:
            model = ReceiverData(ModelName.PUBLISHER).get_by_slug(request.slug)
            form = PublisherForm(instance=model)
        else:
            form = PublisherForm()
        return {
            "form": form,
            "title": "Издательство",
            "name": "Название"
        }

    def publisher_list_to_edit(self, request) -> dict:
        models = ReceiverData(model_name=ModelName.PUBLISHER).get_all()
        url_interspersed = "publisher"
        title = "Издательства"
        return {
            "models": models,
            "url_interspersed": url_interspersed,
            "title": title,
        }

    def book_form_context(self, request) -> dict:
        if request:
            model = ReceiverData(ModelName.BOOK).get_by_slug(request.slug)
            form = BookForm(instance=model)
        else:
            form = BookForm()
        return {
            "form": form,
        }

    def book_list_to_edit(self, request) -> dict:
        models = ReceiverData(model_name=ModelName.BOOK).get_all()
        url_interspersed = "book"
        title = "Книги"
        return {
            "models": models,
            "url_interspersed": url_interspersed,
            "title": title,
        }


    def filter_context(self, request) -> dict:
        return {
            "books": ReceiverData(ModelName.BOOK).get_with_filters(request),
            "form" : FilterForms(),
            "filter" : True,
        }