import django_filters
from django import forms
from .models import Coment


class MyDateInput(forms.DateInput):
    input_type = 'date'


class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = Coment
        fields ={'post_coment': ['exact']}
