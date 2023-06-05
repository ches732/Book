from django.core.exceptions import ObjectDoesNotExist
from .models import Book
from .serializers import BookSerializer


def get_book_id(book_id: int):
    """Получение опроса по id"""
    try:
        return Book.objects.get(book_id=book_id)
    except ObjectDoesNotExist:
        return


def create_book(book: dict):
    """Создание опроса"""
    book = Book.objects.create(
        title=book.get("title"),
        author=book.get("author"),
        genre=book.get("genre"),
        price=book.get("price"),
        release_year=book.get("release_year")
    )
    return book


def update_book(request, book_id: int):
    """Обновление опроса"""
    if not book_id:
        return "Не может быть обновлен"
    book = Book.objects.get(book_id=book_id)
    serializer = BookSerializer(book, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_book(book_id: int):
    """Удаление опроса"""
    book = Book.objects.get(book_id=book_id)
    if book_id != book_id:
        return "Не может быть удален"
    return book.delete()
