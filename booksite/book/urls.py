from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookCreateView.as_view()),
    path('book/<int:id>', views.BookAPIView.as_view()),
    path('book/authors/<int:id>', views.AuthorViewSet.as_view({'get': 'retrieve_author'})),
    path('book/genre/<int:id>', views.GenreViewSet.as_view({'get': 'retrieve_genre'}))
]
