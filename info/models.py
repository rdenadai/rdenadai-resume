from __future__ import unicode_literals
from django.db.models import Model
from django.db.models import CharField, FileField, TextField, IntegerField
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto import S3BotoStorage
from resume import settings


@deconstructible
class MediaS3BotoStorage(S3BotoStorage):
    location: str = "media"


class WhoIAm(Model):
    text: TextField = TextField()

    def __unicode__(self):
        return f"{self.text}"


class Persona(Model):
    upload_storage: MediaS3BotoStorage = MediaS3BotoStorage()

    title: CharField = CharField(max_length=100, unique=True)
    link: CharField = CharField(max_length=255, null=True, blank=True)
    file_link: CharField = CharField(max_length=100, null=True, blank=True)
    file: FileField = FileField(
        upload_to="file/blog/",
        storage=upload_storage,
        default=settings.MEDIA_URL + "/img/flow.jpg",
    )
    body: TextField = TextField()
    order: IntegerField = IntegerField(default=0)

    def __unicode__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering: list = ["order", "title"]


class Curriculum(Model):
    title: CharField = CharField(max_length=100, unique=True)
    body: TextField = TextField()

    def __unicode__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"


class Project(Model):
    title: CharField = CharField(max_length=100, unique=True)
    description: TextField = TextField(max_length=255, null=True, blank=True)
    site: CharField = CharField(max_length=255, null=True, blank=True)
    gplay: CharField = CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"
