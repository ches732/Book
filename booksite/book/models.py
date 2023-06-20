from django.db import models


class Author(models.Model):
    """Author - Автор

    Атрибуты:
        first_name: Имя автора
        last_name: Фамилия автора
        date_of_birth: Дата рождения
        date_of_death: Дата смерти
    """

    first_name = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=True, null=False, default=None, verbose_name='Отчество')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_of_death = models.DateField(null=False, blank=True, verbose_name='Дата смерти')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.middle_name}"


class Genre(models.Model):
    """Genre - Жанр

    Атрибут:
        name:  Название жанра
    """

    name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='Наименование жанра')

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

    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True, verbose_name='Название')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    price = models.IntegerField(blank=True, null=True, default=None, verbose_name='Цена')
    release_year = models.IntegerField(blank=True, null=True, default=None, verbose_name='Год выпуска')

    def __str__(self):
        return self.title
