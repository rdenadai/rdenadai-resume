from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Curriculum, Persona, WhoIAm


class WhoIAmMarkdownModelForm(forms.ModelForm):
    text: forms.CharField = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = WhoIAm
        fields = "__all__"


class PersonaMarkdownModelForm(forms.ModelForm):
    body: forms.CharField = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Persona
        fields = "__all__"


class CurriculumMarkdownModelForm(forms.ModelForm):
    body: forms.CharField = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Curriculum
        fields = "__all__"
