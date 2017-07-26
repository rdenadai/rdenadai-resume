from django.contrib import admin
from .forms import MarkdownModelForm
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    form = MarkdownModelForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
