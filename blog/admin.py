from django.contrib import admin

from blog.models import Blog, Category

from .forms import MarkdownModelForm


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields: dict = {"slug": ("title",)}
    list_display: tuple = ("title", "favorite", "published", "posted")
    form: MarkdownModelForm = MarkdownModelForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields: dict = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
