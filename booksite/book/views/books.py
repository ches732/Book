from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import (
    BookInputSerializer,
    BookSerializer,
    AuthorSerializer,
    GenreSerializer
)
from book.services.authors import (
    get_all_authors_book,
    create_author,
    delete_author
)
from book.services.books import (
    create_book,
    get_all_books,
    update_book,
    delete_book,
    get_filter_book
)
from book.services.genres import (
    delete_genre,
    create_genre,
    get_all_genres_book
)


class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer = BookSerializer

    def create_book(self, request: Request) -> Response:
        """Создание книги"""

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

    def retrieve_all(self, request: Request) -> Response:
        """Получение конкретной книги"""
        book = get_all_books()
        filter_book = get_filter_book(book, request.GET)
        if not book:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(BookSerializer(filter_book, many=True).data, status=status.HTTP_200_OK)

    def update_book(self, request: Request, id: int) -> Response:
        """Редактирование книги"""

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

    def remove_book(self, request: Request, id: int) -> Response:
        """Удаление книги"""

        try:
            delete_book(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)

    def get_authors(self, request: Request, id: int) -> Response:
        """Получение авторов книги"""
        authors = get_all_authors_book(id)
        if not authors:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(AuthorSerializer(authors, many=True).data, status=status.HTTP_200_OK)

    def append_authors(self, request: Request, id: int) -> Response:
        """Добавление авторов"""

        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data
        try:
            author = create_author(author=author, id=id)
        except:
            return Response(
                data={"error": "Ошибка добавлении автора в книгу"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AuthorSerializer(author)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def remove_authors(self, request: Request, id: int) -> Response:
        """Удаление автора"""

        try:
            delete_author(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)

    def get_genres(self, request: Request, id: int) -> Response:
        """Получение жанров книги"""
        genres = get_all_genres_book(id)
        if not genres:
            return Response(
                data={"error": "Объект не найден или не существует"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(GenreSerializer(genres, many=True).data, status=status.HTTP_200_OK)

    def append_genres(self, request: Request, id: int) -> Response:
        """Добавление жанров"""

        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.validated_data
        try:
            genre = create_genre(genre=genre, id=id)
        except:
            return Response(
                data={"error": "Ошибка при создании опроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = GenreSerializer(genre)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def remove_genres(self, request: Request, id: int) -> Response:
        """Удаление жанра"""

        try:
            delete_genre(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)
