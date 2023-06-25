from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from book.models import Book
from book.serializers import (
    BookInputSerializer,
    BookSerializer,
    AuthorSerializer,
    GenreSerializer,
    AuthorIDsSerializer,
    GenreIDsSerializer
)
from book.services.books import (
    create_book,
    get_all_books,
    update_book,
    delete_book,
    get_all_authors_book,
    add_author,
    get_filter_book,
    delete_author,
    get_all_genres_book,
    add_genre,
    delete_genre
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
                data={"error": "Ошибка при создании книги"},
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
                data={"error": "Книга не найдена или не существует"},
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
                data={"error": "Книга не может быть обновлена"},
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
                data={"error": "Книга не может быть удалена"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)

    def get_authors(self, request: Request, id: int) -> Response:
        """Получение авторов по id книги"""
        authors = get_all_authors_book(id)
        if not authors:
            return Response(
                data={"error": "Авторы не найдены или не существуют"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(AuthorSerializer(authors, many=True).data, status=status.HTTP_200_OK)

    def append_authors(self, request: Request, id: int) -> Response:
        """Добавление авторов в книгу"""
        serializer = AuthorIDsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors_ids = serializer.validated_data
        try:
            book = Book.objects.get(id=id)
            add_author(book=book, authors_ids=authors_ids)
        except:
            return Response(
                data={"error": "Ошибка добавления авторов в книгу"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_201_CREATED)

    def remove_authors(self, request: Request, id: int) -> Response:
        """Удаление авторов из книги"""
        serializer = AuthorIDsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors_ids = serializer.validated_data
        try:
            book = Book.objects.get(id=id)
            delete_author(book=book, authors_ids=authors_ids)
        except:
            return Response(
                data={"error": "Авторы не могут быть удалены"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)

    def get_genres(self, request: Request, id: int) -> Response:
        """Получение жанров книги"""
        genres = get_all_genres_book(id)
        if not genres:
            return Response(
                data={"error": "Жанры не найдены или не существуют"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(GenreSerializer(genres, many=True).data, status=status.HTTP_200_OK)

    def append_genres(self, request: Request, id: int) -> Response:
        """Добавление жанров в книгу"""
        serializer = GenreIDsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genres_ids = serializer.validated_data
        print(genres_ids)
        try:
            book = Book.objects.get(id=id)
            add_genre(book=book, genres_ids=genres_ids)
        except:
            return Response(
                data={"error": "Ошибка при добавлении жанров в книгу"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_201_CREATED)

    def remove_genres(self, request: Request, id: int) -> Response:
        """Удаление жанров из книги"""
        serializer = GenreIDsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genres_ids = serializer.validated_data
        try:
            book = Book.objects.get(id=id)
            delete_genre(book=book, genres_ids=genres_ids)
        except:
            return Response(
                data={"error": "Жанры не могут быть удалены"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)
