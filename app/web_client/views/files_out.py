from django.http import FileResponse

from core.file_generator import *
from core.decorators import sending_files_decorator


@sending_files_decorator
def authors_file(request):
    file_name = author_files_generator()
    return FileResponse(open(file_name, 'rb'))


@sending_files_decorator
def genre_file(request):
    file_name = genre_files_generator()
    return FileResponse(open(file_name, 'rb'))


@sending_files_decorator
def publisher_file(request):
    file_name = publisher_files_generator()
    return FileResponse(open(file_name, 'rb'))


@sending_files_decorator
def book_file(request):
    file_name = book_files_generator()
    return FileResponse(open(file_name, 'rb'))