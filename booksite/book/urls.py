from django.urls import path
from .views import authors, books, genres

urlpatterns = [
    path('books/', books.BooksAPIView.as_view()),
    path('book/', books.BookAPIView.as_view()),
    path('book/<int:id>', books.BookAPIView.as_view()),
    path('book/<int:id>/authors', authors.AuthorAPIView.as_view()),
    path('book/<int:id>/genres', genres.GenreAPIView.as_view()),
    path('authors/', authors.AuthorViewSet.as_view(
        {
            'get': 'list'
        }
    )),
    path('authors/<int:id>', authors.AuthorViewSet.as_view(
        {
            'get': 'retrieve'
        }
    )),
    path('genres/', genres.GenreViewSet.as_view(
        {
            'get': 'list'
        }
    )),
    path('genres/<int:id>', genres.GenreViewSet.as_view(
        {
            'get': 'retrieve'
        }
    ))
]
