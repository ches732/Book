from typing import OrderedDict
from rest_framework.exceptions import ValidationError
from book.models import Author, Book


def get_all_authors_book(id: int):
    """Получение авторов по id книги"""

    book = Book.objects.get(id=id)
    authors = book.authors.all()
    return authors


def create_author(author: OrderedDict, id: int):
    """Создание автора по id книги"""

    book = Book.objects.get(id=id)
    authors = book.authors.create(**author)
    return authors


def delete_author(id: int):
    """Удаление автора по id"""

    author = Author.objects.get(id=id)
    if not id:
        raise ValidationError("Автор не может быть удален, укажите id")
    return author.delete()
