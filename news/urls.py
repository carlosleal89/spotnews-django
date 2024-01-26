from django.urls import path
from news.views import index
from news.views import news_details

urlpatterns = [
  path("", index, name="home-page"),
  path("news/<int:news_id>", news_details, name="news-details-page")
]
