from enum import IntEnum

from core.receive_data import ReceiverData, ModelName
from web_client.forms import AuthorForm


class HendlerName(IntEnum):
    INDEX = 1
    AUTHOR_FORM = 2



class ContextFactory:

    def get_context(self, hendler_name:HendlerName, request):
        if hendler_name == HendlerName.INDEX:
            return self.index_context(request)
        elif hendler_name == HendlerName.AUTHOR_FORM:
            pass

    def index_context(self, request) -> dict:
        return {
            "books": ReceiverData(ModelName.BOOK).get_with_terms(request) 
        }

    def author_form_context(self, request) -> dict:
        author_form = AuthorForm()
        return {
            "form" : author_form
        }