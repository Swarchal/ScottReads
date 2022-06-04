import datetime

from django.db import models
from django.utils import timezone


class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        if self.initials is None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.initials} {self.last_name}"

    def name(self) -> str:
        return str(self)


class Genre(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.description)


class Book(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="book")
    pub_date = models.DateField("published date", blank=True, null=True)
    publisher = models.CharField(max_length=100,)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    have_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.title)


class Reading(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    finished_date = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.book} {self.start_date}"

    def has_finished(self) -> bool:
        return self.finished_date is not None

    def is_recent(self) -> bool:
        return self.start_date >= timezone.now() - datetime.timedelta(days=60)
