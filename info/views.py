from django.shortcuts import render

from resume import settings

from .models import Curriculum, Persona, Project


def index(request):
    personas = Persona.objects.all()
    curriculum = Curriculum.objects.all()
    if curriculum:
        curriculum = curriculum[0]
    projects = Project.objects.all().order_by("-score")
    return render(
        request,
        "info/index.html",
        context={
            "MEDIA_URL": settings.MEDIA_URL,
            "resume": curriculum,
            "personas": personas,
            "projects": projects,
            "active_resume": "is-active",
        },
    )
