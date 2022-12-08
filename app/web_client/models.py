from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=250, unique=True,
                            verbose_name="имя/название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Author(BaseModel):
    is_alive = models.BooleanField(default=True)


class Genre(BaseModel):
    pass


class Publisher(BaseModel):
    pass


# TODO: этот пункт надо тоже унаследовать
class Book(models.Model):
    title = models.CharField(
        max_length=250, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()

    author = models.ManyToManyField(
        Author, related_name="authors")
    genre = models.ForeignKey(
        Genre, related_name='books', on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(
        Publisher, related_name='books', on_delete=models.CASCADE, null=True)

    publication_date = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title
