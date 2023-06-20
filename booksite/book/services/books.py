from typing import OrderedDict, List, Dict
from django.db import transaction
from rest_framework.exceptions import ValidationError
from book.models import Book, Author, Genre
from book.services.filter_service import BOOKS_FILTERS


def get_all_books():
    return Book.objects.all()


def create_book(book: OrderedDict):
    """Создание книги"""

    genres = book.get("genres")
    authors = book.get("authors")
    book = Book.objects.create(
        title=book.get("title"),
        price=book.get("price"),
        release_year=book.get("release_year")
    )
    add_authors(book, authors)
    add_genres(book, genres)
    return book


def add_authors(book: Book, authors: List[Dict[str, str]]):
    """Создание атрибутов автора"""

    for key in authors:
        authors_obj = Author.objects.get_or_create(
            first_name=key.get("first_name"),
            last_name=key.get("last_name"),
            date_of_birth=key.get("date_of_birth"),
            date_of_death=key.get("date_of_death")
        )
        book.authors.add(authors_obj[0])


def add_genres(book: Book, genres: List[Dict[str, str]]):
    """Создание атрибута жанра"""

    for key in genres:
        genres_obj = Genre.objects.get_or_create(name=key.get("name"))
        book.genres.add(genres_obj[0])


@transaction.atomic()
def update_book(book: OrderedDict, id: int) -> Book:
    """Обновление книги"""

    genres = book.pop("genres")
    authors = book.pop("authors")
    if not id:
        raise ValidationError("Книга не может быть обновлена, укажите id")
    queryset = Book.objects.filter(id=id)
    queryset.update(**book)
    update_authors(queryset[0], authors, id)
    update_genres(queryset[0], genres, id)
    return queryset[0]


def update_authors(book: Book, authors: List[Dict[str, str]], id: int):
    """Обновление атрибутов автора"""

    for author in authors:
        authors_obj = Author.objects.filter(id=id).update_or_create(**author)
        book.authors.add(authors_obj[0])


def update_genres(book: Book, genres: List[Dict[str, str]], id: int):
    """Обновление атрибута жанра"""

    for genre in genres:
        genre_obj = Genre.objects.filter(id=id).update_or_create(**genre)
        book.genres.add(genre_obj[0])


def delete_book(id: int):
    """Удаление книги"""

    book = Book.objects.get(id=id)
    if not id:
        raise ValidationError("Книга не может быть удалена, укажите id")
    return book.delete()


def get_filter_book(books, book):
    """Фильтрация атрибутов книги"""

    for key in book.keys():
        if key in BOOKS_FILTERS.keys():
            books = BOOKS_FILTERS[key](books, book[key])
    return books
