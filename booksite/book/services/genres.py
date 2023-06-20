from typing import OrderedDict
from rest_framework.exceptions import ValidationError
from book.models import Genre, Book


def get_all_genres_book(id: int):
    """Получение жанров по id книги"""

    book = Book.objects.get(id=id)
    genres = book.genres.all()
    return genres


def create_genre(genre: OrderedDict, id: int):
    """Создание жанров по id книги"""

    book = Book.objects.get(id=id)
    genres = book.genres.create(**genre)
    return genres


def delete_genre(id: int):
    """Удаление жанра по id"""

    genre = Genre.objects.get(id=id)
    if not id:
        raise ValidationError("Автор не может быть удален, укажите id")
    return genre.delete()
