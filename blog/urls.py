# -*- coding: utf-8 -*-

from django.conf.urls import url
import blog.views


urlpatterns = [
    url(r"^$", blog.views.index, name="view_blog_index"),
    url(r"(?P<page>\d{1,3})/$", blog.views.index, name="view_blog_index_page"),
    url(r"^view/(?P<slug>[^\.]+).html", blog.views.view_post, name="view_blog_post"),
    url(
        r"^search/(?P<page>\d{1,3})/(?P<slug>[^\.]+).html",
        blog.views.search_post,
        name="search_blog_post",
    ),
    url(
        r"^search/(?P<slug>[^\.]+).html",
        blog.views.search_post,
        name="search_blog_post",
    ),
    url(
        r"^category/(?P<page>\d{1,3})/(?P<slug>[^\.]+).html",
        blog.views.view_category,
        name="view_blog_category",
    ),
    url(
        r"^category/(?P<slug>[^\.]+).html",
        blog.views.view_category,
        name="view_blog_category",
    ),
]
