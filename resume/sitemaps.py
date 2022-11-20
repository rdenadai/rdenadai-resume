from django.contrib import sitemaps
from django.urls import reverse

from info.views import index


class StaticViewSitemap(sitemaps.Sitemap):
    priority: float = 0.5
    changefreq: str = "daily"

    def items(self):
        return [index]

    def location(self, item):
        return reverse(item)
