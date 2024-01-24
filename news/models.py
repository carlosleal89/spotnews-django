from django.db import models
from news.validators import validate_title


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return f'{self.name}'


class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        validators=[validate_title]
        )
    content = models.TextField(blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news'
        )
    created_at = models.DateField(blank=False)
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(
        Category,
        related_name='news'
        )

    def add_category(self, category):
        self.categories.add(category)
        self.save()

    def remove_category(self, category):
        self.categories.remove(category)
        self.save()

    def __str__(self) -> str:
        return f'{self.title}'
