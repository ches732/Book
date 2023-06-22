from rest_framework import viewsets, status
from rest_framework.response import Response
from book.models import Genre
from book.serializers import GenreSerializer
from book.services.genres import (
    create_genre,
    update_genre,
    delete_genre,
    retrieve_genre
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def list(self, request, *args, **kwargs):
        """Получение списка жанров книг"""
        queryset = self.get_queryset()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Создание жанра"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors = create_genre(serializer.validated_data)
        serializer = GenreSerializer(authors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        """Получение жанров по id"""
        genres = retrieve_genre(**kwargs)
        serializer = self.get_serializer(genres)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Обновление жанров по id"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors = update_genre(serializer.validated_data, **kwargs)
        serializer = GenreSerializer(authors)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Удаление жанров по id"""
        delete_genre(**kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)