from pagedown.widgets import AdminPagedownWidget
from django import forms
from .models import Blog


class MarkdownModelForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Blog
        fields = '__all__'
