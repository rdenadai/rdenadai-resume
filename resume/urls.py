"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index as blog_index

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

from blog.models import Blog, Category

blog_dict = {
    "queryset": Blog.objects.all(),
    "date_field": "posted",
}
category_dict = {
    "queryset": Category.objects.all(),
    "date_field": "posted",
}

admin.site.site_header = "rdenadai.com"
handler403 = "blog.views.view_400"
handler403 = "blog.views.view_403"
handler404 = "blog.views.view_404"
handler500 = "blog.views.view_500"

admin_url = os.environ.get("ADMIN", "admin")

urlpatterns = [
    url(r"^$", blog_index, name="view_index"),
    url(r"^{}/".format(admin_url), admin.site.urls),
    url(r"^info/", include("info.urls")),
    url(r"^blog/", include("blog.urls")),
    url(
        r"^sitemap\.xml$",
        sitemap,
        {
            "sitemaps": {
                "static": StaticViewSitemap,
                "blog": GenericSitemap(blog_dict, priority=0.6),
                "category": GenericSitemap(category_dict, priority=0.6),
            }
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
    url(
        r"^robots\.txt$",
        TemplateView.as_view(
            template_name="resume/robots.txt", content_type="text/plain"
        ),
        name="robots.txt",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
