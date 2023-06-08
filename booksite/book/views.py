from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

from .models import Author, Genre
from .serializers import BookSerializer, BookInputSerializer, AuthorSerializer, GenreSerializer
from book.services.service import (
    create_book,
    update_book,
    delete_book,
    get_all_books,
    get_filter_book,
)


class BookCreateView(APIView):
    def post(self, request: Request) -> Response:
        """Создание опроса"""
        serializer = BookInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data
        print(book)
        try:
            book = create_book(book=book)
        except Exception as ex:
            print(ex)
            return Response(
                data={"error": "Ошибка при создании опроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BookSerializer(book)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        """Получение опроса"""
        book = get_all_books()
        filter_book = get_filter_book(book, request.GET)
        if not book:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(BookSerializer(filter_book, many=True).data, status=status.HTTP_200_OK)


class BookAPIView(APIView):

    def put(self, request: Request, id: int) -> Response:
        """Редактирование опроса"""
        try:
            book = update_book(request, id=id)
        except Exception as ex:
            print(ex)
            return Response(
                data={"error": "Объект не может быть обновлен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(book, status=status.HTTP_200_OK)

    def delete(self, request: Request, id: int) -> Response:
        """Удаление опроса"""
        try:
            delete_book(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)


class AuthorViewSet(viewsets.ViewSet):
    """Получение авторов по id книги"""
    def retrieve_author(self, request: Request, id: int) -> Response:
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, id=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenreViewSet(viewsets.ViewSet):
    """Получение жанров по id книги"""
    def retrieve_genre(self, request: Request, id: int) -> Response:
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, id=id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)
