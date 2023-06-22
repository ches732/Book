from typing import OrderedDict
from book.models import Genre


def retrieve_genre(pk: int):
    """Получение жанра по id"""
    genre = Genre.objects.get(pk=pk)
    return genre


def create_genre(genre: OrderedDict):
    """Создание жанра"""
    authors = Genre.objects.create(**genre)
    return authors


def update_genre(genre: OrderedDict, pk: int):
    """Обновление жанра по id"""
    genres = Genre.objects.filter(pk=pk)
    genres.update(**genre)
    return genres[0]


def delete_genre(pk: int):
    """Удаление жанра по id"""
    genre = Genre.objects.filter(pk=pk)
    return genre.delete()
