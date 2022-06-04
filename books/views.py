from django.views import generic

from . import models


class IndexView(generic.TemplateView):
    template_name = "books/index.html"


class BookListView(generic.ListView):
    model = models.Book
    template_name = "books/books.html"


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = "books/book.html"


class AuthorListView(generic.ListView):
    model = models.Author
    template_name = "books/authors.html"

    ordering = ["last_name", "first_name"]


class AuthorDetailView(generic.DetailView):
    model = models.Author
    template_name = "books/author.html"


class CurrentlyReadingView(generic.ListView):
    model = models.Reading
    template_name = "books/currently_reading.html"

    def get_queryset(self):
        """filter on having a start date but no end date"""
        return models.Reading.objects.filter(finished_date__isnull=True)


class ToReadView(generic.ListView):
    model = models.Book
    template_name = "books/to_read.html"

    def get_queryset(self):
        return models.Book.objects.filter(have_read=False)


class HaveReadView(generic.ListView):
    model = models.Book
    template_name = "books/have_read.html"

    def get_queryset(self):
        return models.Book.objects.filter(have_read=True)
