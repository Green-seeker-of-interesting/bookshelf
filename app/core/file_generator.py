import uuid
import os

import pandas as pd

from core.receive_data import ReceiverData, ModelName


def author_files_generator() -> str:
    items = []
    models = ReceiverData(model_name=ModelName.AUTHOR).get_all()
    for item in models:
        items.append((
            item.name,
            item.description,
        ))
    df = pd.DataFrame(items, columns=("ФИО", "Описание"))
    file_name = os.path.join("temporary_files", str(uuid.uuid4()) + ".xlsx")
    df.to_excel(file_name)
    return file_name


def genre_files_generator() -> str:
    items = []
    models = ReceiverData(model_name=ModelName.GENRE).get_all()
    for item in models:
        items.append((
            item.name,
            item.description,
        ))
    df = pd.DataFrame(items, columns=("Название", "Описание"))
    file_name = os.path.join("temporary_files", str(uuid.uuid4()) + ".xlsx")
    df.to_excel(file_name)
    return file_name


def publisher_files_generator() -> str:
    items = []
    models = ReceiverData(model_name=ModelName.PUBLISHER).get_all()
    for item in models:
        items.append((
            item.name,
            item.description,
        ))
    df = pd.DataFrame(items, columns=("Название", "Описание"))
    file_name = os.path.join("temporary_files", str(uuid.uuid4()) + ".xlsx")
    df.to_excel(file_name)
    return file_name


def book_files_generator() -> str:
    items = []
    models = ReceiverData(model_name=ModelName.BOOK).get_all()
    for item in models:
        items.append((
            item.title,
            item.description,
            item.genre.name,
            item.publisher.name,
            author_to_str(item)
        ))
    df = pd.DataFrame(items, columns=("ФИО", "Описание",
                      "Жанр", "Издательство", "Авторы"))
    file_name = os.path.join("temporary_files", str(uuid.uuid4()) + ".xlsx")
    df.to_excel(file_name)
    return file_name


def author_to_str(models):
    out = ""
    for author in models.author.all():
        out += author.name + "\n"
    return out
