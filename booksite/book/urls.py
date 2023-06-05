from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookCreateView.as_view()),
    path('book/<int:book_id>', views.BookAPIView.as_view()),
]
