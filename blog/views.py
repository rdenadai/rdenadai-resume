# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Category
from info.models import WhoIAm
from resume import settings
from datetime import date
from django.db.models import Q


def index(request, page=0):
    publications = Blog.objects.filter(published=True).order_by("-posted")
    qtd_publications = publications.count()
    page = int(page)
    inicio = page * 5
    fim = inicio + 5
    previous_page = True if page > 0 else False
    next_page = True if qtd_publications > fim else False
    before_page = page - 1
    after_page = page + 1

    whoiam = ""
    whoiams = WhoIAm.objects.all()
    for hist in whoiams:
        whoiam += hist.text

    return render(
        request,
        "blog/index.html",
        context={
            "MEDIA_URL": settings.MEDIA_URL,
            "qtd_publications": qtd_publications,
            "publications": publications[inicio:fim],
            "previous_page": previous_page,
            "next_page": next_page,
            "before_page": before_page,
            "after_page": after_page,
            "whoiam": whoiam,
            "active_essays": "is-active",
        },
    )


def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    now = date.today()
    days_ago = (now - post.posted).days
    return render(
        request,
        "blog/view_post.html",
        {
            "MEDIA_URL": settings.MEDIA_URL,
            "post": post,
            "days_ago": days_ago,
            "active_essays": "is-active",
        },
    )


def search_post(request, slug, page=1):
    publications = (
        Blog.objects.filter(published=True)
        .filter(
            Q(body__icontains=slug)
            | Q(body__istartswith=slug)
            | Q(body__iendswith=slug)
            | Q(category__in=list(Category.objects.filter(name__icontains=slug)))
        )
        .distinct()
        .order_by("-posted")
    )
    qtd_publications = publications.count()
    page = int(page)
    start = page - 1
    limit = 5 * page
    previous_page = True if page > 1 else False
    next_page = True if qtd_publications > limit else False
    before_page = page - 1
    after_page = page + 1

    whoiam = ""
    whoiams = WhoIAm.objects.all()
    for hist in whoiams:
        whoiam += hist.text

    return render(
        request,
        "blog/index.html",
        context={
            "MEDIA_URL": settings.MEDIA_URL,
            "qtd_publications": qtd_publications,
            "publications": publications[start:limit],
            "previous_page": previous_page,
            "next_page": next_page,
            "before_page": before_page,
            "after_page": after_page,
            "active_essays": "is-active",
            "whoiam": whoiam,
        },
    )


def view_category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug)
    publications = Blog.objects.filter(published=True, category=category).order_by(
        "-posted"
    )
    qtd_publications = publications.count()
    page = int(page)
    start = page - 1
    limit = 5 * page
    previous_page = True if page > 1 else False
    next_page = True if qtd_publications > limit else False
    before_page = page - 1
    after_page = page + 1
    return render(
        request,
        "blog/view_category.html",
        context={
            "MEDIA_URL": settings.MEDIA_URL,
            "category": category,
            "qtd_publications": qtd_publications,
            "publications": publications[start:limit],
            "previous_page": previous_page,
            "next_page": next_page,
            "before_page": before_page,
            "after_page": after_page,
            "active_essays": "is-active",
        },
    )


def view_400(request, exception):
    response = render(request, "blog/400.html")
    response.status_code = 400
    return response


def view_403(request, exception):
    response = render(request, "blog/403.html")
    response.status_code = 403
    return response


def view_404(request, exception):
    response = render(request, "blog/404.html")
    response.status_code = 404
    return response


def view_500(request):
    response = render(request, "blog/500.html")
    response.status_code = 500
    return response
