from django.contrib import admin
from news.models import News
from news.models import Category

admin.site.register(News)
admin.site.register(Category)
