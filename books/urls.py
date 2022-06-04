from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("author/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("to_read/", views.ToReadView.as_view(), name="to-read"),
    path("currently_reading/", views.CurrentlyReadingView.as_view(), name="currently-reading"),
    path("have_read/", views.HaveReadView.as_view(), name="have-read"),
]
