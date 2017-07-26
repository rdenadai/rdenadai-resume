# -*- coding: utf-8 -*-

from django.shortcuts import render
from resume import settings
from .models import Persona, Curriculum, Project


def index(request):
    personas = Persona.objects.all()
    curriculum = Curriculum.objects.all()
    if curriculum:
        curriculum = curriculum[0]
    projects = Project.objects.all()
    return render(request, 'info/index.html', context={
        'MEDIA_URL': settings.MEDIA_URL,
        'resume': curriculum,
        'personas': personas,
        'projects': projects,
        'active_resume': 'is-active'
    })
