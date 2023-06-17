from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Author
from book.serializers import AuthorSerializer
from book.services.authors import (
    create_author,
    update_author,
    delete_author
)


class AuthorAPIView(APIView):
    def post(self, request: Request, id: int) -> Response:
        """Создание запроса"""

        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data
        try:
            author = create_author(author=author)
        except:
            return Response(
                data={"error": "Ошибка при создании запроса"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AuthorSerializer(author)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: Request, id: int) -> Response:
        """Обновление запроса"""

        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.validated_data
        try:
            author = update_author(author=author, id=id)
        except:
            return Response(
                data={"error": "Объект не может быть обновлен"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AuthorSerializer(author)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request: Request, id: int) -> Response:
        """Удаление запроса"""

        try:
            delete_author(id)
        except Exception as ex:
            return Response(
                data={"error": "Объект не может быть удален"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_200_OK)


class AuthorViewSet(viewsets.ViewSet):
    def retrieve(self, request: Request, id: int) -> Response:
        """Получение авторов по id """

        queryset = Author.objects.all()
        author = get_object_or_404(queryset, id=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request) -> Response:
        """Получение всех авторов"""
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
