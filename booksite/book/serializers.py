from rest_framework import serializers
from .models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "middle_name", "date_of_birth", "date_of_death"]


class AuthorIDsSerializer(serializers.Serializer):
    author_ids = serializers.ListField(child=serializers.IntegerField())


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class GenreIDsSerializer(serializers.Serializer):
    genre_ids = serializers.ListField(child=serializers.IntegerField())


class BookInputSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
