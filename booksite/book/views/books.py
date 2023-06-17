from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Book
from book.serializers import BookInputSerializer, BookSerializer
from book.services.books import (
    create_book,
    get_all_books,
    update_book,
    delete_book, get_filter_book
)


class BooksAPIView(APIView):
    queryset = get_all_books()
    serializer_class = BookSerializer

    def post(self, request: Request) -> Response:
        """Создание запроса"""

        serializer = BookInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data
        try:
            book = create_book(book=book)
        except:
            return Response(
                data={"error": "Ошибка при создании запроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        """Получение запроса со всеми книгами"""

        books = get_all_books()
        if not books:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(BookSerializer(books, many=True).data, status=status.HTTP_200_OK)


class BookAPIView(APIView):
    queryset = Book.objects.all()
    serializer = BookSerializer

    def post(self, request: Request) -> Response:
        """Создание запроса"""

        serializer = BookInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data
        try:
            book = create_book(book=book)
        except:
            return Response(
                data={"error": "Ошибка при создании запроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        """Получение запроса на конкретную книгу"""
        book = get_all_books()
        filter_book = get_filter_book(book, request.GET)
        if not book:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(BookSerializer(filter_book, many=True).data, status=status.HTTP_200_OK)

    def put(self, request: Request, id: int) -> Response:
        """Редактирование запроса"""

        serializer = BookInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data
        try:
            book = update_book(book=book, id=id)
        except:
            return Response(
                data={"error": "Объект не может быть обновлен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, id: int) -> Response:
        """Удаление запроса"""

        try:
            delete_book(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)
