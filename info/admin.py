from django.contrib import admin
from .forms import (
    WhoIAmMarkdownModelForm,
    PersonaMarkdownModelForm,
    CurriculumMarkdownModelForm,
)
from info.models import WhoIAm, Persona, Curriculum, Project


class WhoIAmAdmin(admin.ModelAdmin):
    form: WhoIAmMarkdownModelForm = WhoIAmMarkdownModelForm


class PersonaAdmin(admin.ModelAdmin):
    form: PersonaMarkdownModelForm = PersonaMarkdownModelForm


class CurriculumAdmin(admin.ModelAdmin):
    form: CurriculumMarkdownModelForm = CurriculumMarkdownModelForm


class ProjectAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "site", "gplay")


admin.site.register(WhoIAm, WhoIAmAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Project, ProjectAdmin)
