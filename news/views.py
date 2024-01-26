from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from news.models import News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, news_id):
    try:
        news = get_object_or_404(News, id=news_id)
        categories = news.categories.all()
        context = {"news": news, "categories": categories}
        return render(request, 'news_details.html', context)
    except Http404:
        return render(request, '404.html')
