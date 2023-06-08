"""Фильтрация атрибутов"""


def get_filter_by_title(book, title):
    return book.filter(title=title)


def get_filter_by_author(book, authors):
    return book.filter(authors=authors)


def get_filter_by_genre(book, genres):
    return book.filter(genres=genres)


def get_filter_by_price(book, price, operator=None):
    if operator == '>':
        return book.filter(price__gt=price)
    if operator == '<':
        return book.filter(price__lt=price)
    return book.filter(price=price)


def get_filter_by_release_year(book, release_year, operator=None):
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
