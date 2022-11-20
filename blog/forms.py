from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Blog


class MarkdownModelForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model: Blog = Blog
        fields: str = "__all__"
