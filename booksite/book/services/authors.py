from typing import OrderedDict
from book.models import Author


def retrieve_author(pk: int):
    """Получение автора по id"""
    author = Author.objects.get(pk=pk)
    return author


def create_author(author: OrderedDict):
    """Создание автора"""
    authors = Author.objects.create(**author)
    return authors


def update_author(author: OrderedDict, pk: int):
    """Обновление автора по id"""
    authors = Author.objects.filter(pk=pk)
    authors.update(**author)
    return authors[0]


def delete_author(pk: int):
    """Удаление автора по id"""
    author = Author.objects.filter(pk=pk)
    return author.delete()
