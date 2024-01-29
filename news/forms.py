from news.models import Category
from django import forms


class create_categories_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Nome"}
