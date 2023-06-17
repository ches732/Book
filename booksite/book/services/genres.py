from typing import OrderedDict
from rest_framework.exceptions import ValidationError
from book.models import Genre


def create_genre(genre: OrderedDict):
    """Создание атрибутов автора"""

    genre = Genre.objects.create(
        first_name=genre.get("first_name"),
        last_name=genre.get("last_name"),
        date_of_birth=genre.get("date_of_birth"),
        date_of_death=genre.get("date_of_death")
    )
    return genre


def update_genre(genre: OrderedDict, id):
    """Создание  обновление атрибутов автора"""

    if not id:
        raise ValidationError("Автор не может быть обновлен, укажите id")
    queryset = Genre.objects.filter(id=id)
    queryset.update(**genre)
    return queryset[0]


def delete_genre(id: int):
    """Удаление запроса"""

    genre = Genre.objects.get(id=id)
    if not id:
        raise ValidationError("Автор не может быть удален, укажите id")
    return genre.delete()

