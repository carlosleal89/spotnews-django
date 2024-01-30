from django.urls import path
from news.views import index
from news.views import news_details
from news.views import new_category_form, create_news_form

urlpatterns = [
  path("", index, name="home-page"),
  path("news/<int:news_id>", news_details, name="news-details-page"),
  path("categories/", new_category_form, name="categories-form"),
  path("news/", create_news_form, name="news-form"),
]
