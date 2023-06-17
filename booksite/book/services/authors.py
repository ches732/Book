from typing import OrderedDict
from rest_framework.exceptions import ValidationError
from book.models import Author


def create_author(author: OrderedDict):
    """Создание атрибутов автора"""

    author = Author.objects.create(
        first_name=author.get("first_name"),
        last_name=author.get("last_name"),
        date_of_birth=author.get("date_of_birth"),
        date_of_death=author.get("date_of_death")
    )
    return author


def update_author(author: OrderedDict, id):
    """Создание  обновление атрибутов автора"""

    if not id:
        raise ValidationError("Автор не может быть обновлен, укажите id")
    queryset = Author.objects.filter(id=id)
    queryset.update(**author)
    return queryset[0]


def delete_author(id: int):
    """Удаление запроса"""

    author = Author.objects.get(id=id)
    if not id:
        raise ValidationError("Автор не может быть удален, укажите id")
    return author.delete()
