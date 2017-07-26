from __future__ import unicode_literals
from django.db import models
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto import S3BotoStorage
from resume import settings


@deconstructible
class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'


class WhoIAm(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return '%s' % self.text


class Persona(models.Model):
    upload_storage = MediaS3BotoStorage()

    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    file_link = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='file/blog/', storage=upload_storage, default=settings.MEDIA_URL + '/img/flow.jpg')
    body = models.TextField()
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['order', 'title']


class Curriculum(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()

    def __unicode__(self):
        return '%s' % self.title


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    gplay = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title
