from django.contrib import admin

from info.models import Curriculum, Persona, Project, WhoIAm

from .forms import CurriculumMarkdownModelForm, PersonaMarkdownModelForm, WhoIAmMarkdownModelForm


class WhoIAmAdmin(admin.ModelAdmin):
    form: WhoIAmMarkdownModelForm = WhoIAmMarkdownModelForm


class PersonaAdmin(admin.ModelAdmin):
    form: PersonaMarkdownModelForm = PersonaMarkdownModelForm


class CurriculumAdmin(admin.ModelAdmin):
    form: CurriculumMarkdownModelForm = CurriculumMarkdownModelForm


class ProjectAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "score", "site", "gplay")


admin.site.register(WhoIAm, WhoIAmAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Project, ProjectAdmin)
