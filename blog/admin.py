from django.contrib import admin
from .forms import MarkdownModelForm
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    exclude: list = ["posted"]
    prepopulated_fields: dict = {"slug": ("title",)}
    form: MarkdownModelForm = MarkdownModelForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields: dict = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
