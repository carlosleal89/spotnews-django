from news.models import Category, News
from django import forms
from django.forms import CheckboxSelectMultiple


class CreateCategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Nome"}


class CreateNewsForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple(),
        label="Categorias"
    )

    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem"
        }
        widgets = {
            "created_at": forms.DateInput(
                attrs={"type": "date"}
            )
        }
