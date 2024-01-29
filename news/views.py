from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from news.models import News, Category
from news.forms import create_categories_form


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


def new_category_form(request):
    form = create_categories_form()
    if request.method == "POST":
        form = create_categories_form(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)
