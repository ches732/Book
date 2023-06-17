from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Genre
from book.serializers import GenreSerializer
from book.services.genres import (
    create_genre,
    update_genre,
    delete_genre
)


class GenreAPIView(APIView):
    def post(self, request: Request) -> Response:
        """Создание запроса"""

        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.validated_data
        try:
            genre = create_genre(genre=genre)
        except:
            return Response(
                data={"error": "Ошибка при создании опроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = GenreSerializer(genre)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: Request, id) -> Response:
        """Обновление запроса"""

        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        genre = serializer.validated_data
        try:
            genre = update_genre(genre=genre, id=id)
        except:
            return Response(
                data={"error": "Ошибка при создании опроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = GenreSerializer(genre)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request: Request, id) -> Response:
        """Удаление запроса"""

        try:
            delete_genre(id)
        except:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)


class GenreViewSet(viewsets.ViewSet):
    def retrieve(self, request: Request, id: int) -> Response:
        """Получение жанров по id"""

        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, id=id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request) -> Response:
        """Получение списка жанров"""

        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)