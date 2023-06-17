from django.db import models


class Author(models.Model):
    """Author - Автор

    Атрибуты:
        first_name: Имя автора
        last_name: Фамилия автора
        date_of_birth: Дата рождения
        date_of_death: Дата смерти
    """

    first_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Genre(models.Model):
    """Genre - Жанр

    Атрибут:
        name: Жанр
    """

    name = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book - Книга

    Атрибуты:
        title: Заголовок книги
        authors: Авторы книги
        genres: Жанры книги
        price: Цена книги
        release_year: Год выпуска книги
    """

    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    price = models.IntegerField(blank=True, null=True, default=None)
    release_year = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title
