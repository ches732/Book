from typing import OrderedDict, List, Dict
from django.db import transaction
from rest_framework.exceptions import ValidationError
from book.models import Book, Author, Genre
from book.services.filter_service import BOOKS_FILTERS


def get_all_books():
    return Book.objects.all()


def create_book(book: OrderedDict):
    """Создание атрибутов книги"""
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
    for author in authors:
        authors_obj = Author.objects.get_or_create(**author)
        book.authors.add(authors_obj[0])


def add_genres(book: Book, genres: List[Dict[str, str]]):
    """Создание атрибута жанра"""
    for genre in genres:
        genres_obj = Genre.objects.get_or_create(**genre)
        book.genres.add(genres_obj[0])


@transaction.atomic()
def update_book(book: OrderedDict, id: int) -> Book:
    """Обновление атрибутов книги"""
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
        authors_obj = Author.objects.filter(id=id).update(**author)
        book.authors.add(authors_obj)


def update_genres(book: Book, genres: List[Dict[str, str]], id: int):
    """Обновление атрибута жанра"""
    for genre in genres:
        genre_obj = Genre.objects.filter(id=id).update(**genre)
        book.genres.add(genre_obj)


def delete_book(id: int):
    """Удаление книги"""
    book = Book.objects.get(id=id)
    if not id:
        raise ValidationError("Книга не может быть удалена, укажите id")
    return book.delete()


def get_all_authors_book(id: int):
    """Получение авторов по id книги"""
    book = Book.objects.get(id=id)
    authors = book.authors.all()
    return authors


def add_author(book: Book, authors_ids: List[int]):
    """Добавление авторов в книгу"""
    authors_ids = authors_ids.get("author_ids")
    for author_id in authors_ids:
        try:
            book.authors.add(author_id)
        except:
            return f'Автор с id {author_id} не найден'


def delete_author(book: Book, authors_ids: List[int]):
    """Удаление авторов из книги"""
    authors_ids = authors_ids.get("author_ids")
    for author_id in authors_ids:
        try:
            book.authors.remove(author_id)
        except:
            return f'Автор с id {author_id} не найден'


def get_all_genres_book(id: int):
    """Получение жанров по id книги"""
    book = Book.objects.get(id=id)
    genres = book.genres.all()
    return genres


def add_genre(book: Book, genres_ids: List[int]):
    """Добавление жанров в книгу"""
    genres_ids = genres_ids.get("genre_ids")
    for genre_id in genres_ids:
        try:
            book.genres.add(genre_id)
        except:
            return f'Жанр с id {genre_id} не найден'


def delete_genre(book: Book, genres_ids: List[int]):
    """Удаление жанров из книги"""
    genres_ids = genres_ids.get("genre_ids")
    for genre_id in genres_ids:
        try:
            book.genres.remove(genre_id)
        except:
            return f'Жанр с id {genre_id} не найден'


def get_filter_book(books, book):
    """Фильтрация атрибутов книги"""
    for key in book.keys():
        if key in BOOKS_FILTERS.keys():
            books = BOOKS_FILTERS[key](books, book[key])
    return books
