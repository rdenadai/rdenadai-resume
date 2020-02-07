from __future__ import unicode_literals

from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class BlogConfig(AppConfig):
    name: str = "blog"


class SuitConfig(DjangoSuitConfig):
    layout: str = "horizontal"
