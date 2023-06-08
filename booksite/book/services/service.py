from book.services.filter_service import BOOKS_FILTERS
from book.models import Book, Genre, Author
from book.serializers import BookSerializer


def get_all_books():
    return Book.objects.all()


def create_book(book: dict):
    """Создание опроса"""
    genres = book.get("genres")
    authors = book.get("authors")

    book = Book.objects.create(
        title=book.get("title"),
        price=book.get("price"),
        release_year=book.get("release_year")
    )
    add_author(book, authors)
    add_genre(book, genres)
    return book


def add_author(book: Book, authors: list):
    """Создание атрибутов автора"""
    author_list = authors[0]
    author_obj = Author.objects.create(
        first_name=author_list.get("first_name"),
        last_name=author_list.get("last_name"),
        date_of_birth=author_list.get("date_of_birth"),
        date_of_death=author_list.get("date_of_death")
    )
    book.authors.add(author_obj)


def add_genre(book: Book, genres: list):
    """Создание атрибута жанра"""
    genre_list = genres[0]
    genre_obj = Genre.objects.create(genre=genre_list.get("genre"))
    book.genres.add(genre_obj)


def update_book(request, id: int):
    """Обновление опроса"""
    if not id:
        return "Не может быть обновлен"
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_book(id: int):
    """Удаление опроса"""
    book = Book.objects.get(id=id)
    if id != id:
        return "Не может быть удален"
    return book.delete()


def get_filter_book(books, book):
    """Фильтрация атрибутов книги"""
    for key in book.keys():
        if key in BOOKS_FILTERS.keys():
            books = BOOKS_FILTERS[key](books, book[key])
    return books
