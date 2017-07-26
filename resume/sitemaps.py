from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from info.views import index


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [index]

    def location(self, item):
        return reverse(item)
