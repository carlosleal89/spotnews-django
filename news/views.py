from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from news.models import News, Category, User
from news.forms import CreateCategoriesForm, CreateNewsForm
from rest_framework import viewsets
from news.serializers import CategorySerializer, UserSerializer, NewsSerializer


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
    form = CreateCategoriesForm()
    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}
    return render(request, "categories_form.html", context)


def create_news_form(request):
    form = CreateNewsForm()
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        # lembrar de passar o request.FILES quando lidar com arquivos
        if form.is_valid():
            news = form.save(commit=False)
            news.save()

            selected_categories = form.cleaned_data['categories']

            news.categories.set(selected_categories)

            return redirect("home-page")

    context = {"form": form}
    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
