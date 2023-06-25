from rest_framework import viewsets, status
from rest_framework.response import Response
from book.models import Author
from book.serializers import AuthorSerializer
from book.services.authors import (
    create_author,
    update_author,
    delete_author,
    retrieve_author
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """Получение списка авторов книг"""
        queryset = self.get_queryset()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        """Создание автора"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors = create_author(serializer.validated_data)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs) -> Response:
        """Получение автора по id"""
        authors = retrieve_author(**kwargs)
        serializer = self.get_serializer(authors)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs) -> Response:
        """Обновление авторов по id"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authors = update_author(serializer.validated_data, **kwargs)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Удаление авторов по id"""
        delete_author(**kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)




