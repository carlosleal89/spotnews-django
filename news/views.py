from django.shortcuts import render
from news.models import News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)
