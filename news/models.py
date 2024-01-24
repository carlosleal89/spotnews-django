from django.db import models


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
    title = models.CharField(max_length=200, blank=False)
    content = models.CharField(blank=False)
    author = models.ForeignKey('User')
    created_at = models.DateField(blank=False)
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ForeignKey('Category')

    def __str__(self) -> str:
        return f'{self.title}'
