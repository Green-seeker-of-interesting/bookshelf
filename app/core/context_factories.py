from enum import IntEnum


from core.receive_data import ReceiverData, ModelName
from web_client.forms import AuthorForm


class HendlerName(IntEnum):
    INDEX = 1
    AUTHOR_FORM = 2
    AUTHOR_LIST_TO_EDIT = 3
    AUTHOR_EDIT = 4


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

    def index_context(self, request) -> dict:
        return {
            "books": ReceiverData(ModelName.BOOK).get_with_terms(request)
        }

    def author_form_context(self, request) -> dict:
               
        if request:
            author = ReceiverData(ModelName.AUTHOR).get_by_slug(request.slug)
            author_form = AuthorForm(instance=author) 
        else:
            author_form = AuthorForm() 

        return {
            "form": author_form
        }

    def author_list_to_edit(self, request) -> dict:
        models = ReceiverData(model_name=ModelName.AUTHOR).get_all()
        url_interspersed = "author"
        title = "Авторы"
        return {
            "models": models,
            "url_interspersed": url_interspersed,
            "title": title,
        }
