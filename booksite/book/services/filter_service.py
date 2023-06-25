"""Фильтрация атрибутов"""


def get_filter_by_title(book, title):
    """Фильтрация заголовка книги"""
    return book.filter(title=title)


def get_filter_by_author(book, authors):
    """Фильтрация атрибутов авторов книги"""
    return book.filter(authors__first_name__in=authors.split(", "),
                       authors__last_name__in=authors.split(", "),
                       authors__date_of_birth__in=authors.split(", "),
                       authors__date_of_death__in=authors.split(", "))


def get_filter_by_genre(book, genres):
    """Фильтрация атрибута жанра книги"""
    return book.filter(genres__first_name__in=genres.split(", "))


def get_filter_by_price(book, price, operator=None):
    """Фильтрация цены книги"""
    if operator == '>':
        return book.filter(price__gt=price)
    if operator == '<':
        return book.filter(price__lt=price)
    return book.filter(price=price)


def get_filter_by_release_year(book, release_year, operator=None):
    """Фильтрация года выпуска книги"""
    if operator == '>':
        return book.filter(release_year__gt=release_year)
    if operator == '<':
        return book.filter(release_year__lt=release_year)
    return book.filter(release_year=release_year)


BOOKS_FILTERS = {
    'title': get_filter_by_title,
    'author': get_filter_by_author,
    'genre': get_filter_by_genre,
    'price': get_filter_by_price,
    'release_year': get_filter_by_release_year,
}
