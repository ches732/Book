from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookSerializer
from .service import (
    get_book_id,
    create_book,
    update_book,
    delete_book
)


class BookCreateView(APIView):
    def post(self, request: Request) -> Response:
        """Создание опроса"""
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data
        try:
            book = create_book(book=book)
        except:
            return Response(
                data={"error": "Ошибка при создании опроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class BookAPIView(APIView):
    def get(self, request: Request, book_id: int) -> Response:
        """Получение опроса"""
        book = get_book_id(book_id)
        if not book:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, book_id: int) -> Response:
        """Редактирование опроса"""
        try:
            book = update_book(request, book_id=book_id)
        except:
            return Response(
                data={"error": "Объект не может быть обновлен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(book, status=status.HTTP_200_OK)

    def delete(self, request: Request, book_id: int) -> Response:
        """Удаление опроса"""
        try:
            delete_book(book_id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)
