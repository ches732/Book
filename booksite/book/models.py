from django.db import models


class Book(models.Model):
    """Book - Опрос

    Атрибуты:
        book_id: Идентификатор
        title: Заголовок книги
        author: Автор книги
        genre: Жанр книги
        price: Цена книги
        release_year: Год выпуска книги
    """

    book_id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    author = models.CharField(max_length=50, blank=True, null=True, default=None)
    genre = models.CharField(max_length=100, blank=True, null=True, default=None)
    price = models.IntegerField(blank=True, null=True, default=None)
    release_year = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title
