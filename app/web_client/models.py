from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Автор")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()
    is_alive = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Издатель")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="URL")
    description = models.TextField()

    author = models.ManyToManyField(Author, related_name="authors")
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.SET_NULL, null=True)

    publication_date = models.DateField()

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title
    