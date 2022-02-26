from django import forms
from article.models import articlemodel, commments


class articleform(forms.ModelForm):
    class Meta:
        model = articlemodel
        fields = ['title', 'author', 'adesc']
