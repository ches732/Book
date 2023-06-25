from django.urls import path
from .views import authors, books, genres

urlpatterns = [
    path('book/', books.BookAPIView.as_view(
        {
            "get": "retrieve_all",
            "post": "create_book"
        }
    )),
    path('book/<int:id>', books.BookAPIView.as_view(
        {
            "put": "update_book",
            "delete": "remove_book"
        }
    )),
    path('book/<int:id>/authors', books.BookAPIView.as_view(
        {
            "get": "get_authors",
            "post": "append_authors",
            "delete": "remove_authors"
        }
    )),
    path('book/<int:id>/genres', books.BookAPIView.as_view(
        {
            "get": "get_genres",
            "post": "append_genres",
            "delete": "remove_genres"
        }
    )),
    path('authors/', authors.AuthorViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    )),
    path('authors/<int:pk>', authors.AuthorViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy"
        }
    )),
    path('genres/', genres.GenreViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    )),
    path('genres/<int:pk>', genres.GenreViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy"
        }
    ))
]
