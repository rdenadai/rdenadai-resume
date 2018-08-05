from __future__ import unicode_literals
from django.utils.deconstruct import deconstructible
from django.db import models
"""Custom S3 storage backends to store files in subfolders."""
from storages.backends.s3boto import S3BotoStorage
from resume import settings


@deconstructible
class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, db_index=True)
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.name

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})

    class Meta:
        ordering = ['name']


class Blog(models.Model):
    upload_storage = MediaS3BotoStorage()

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to='img/blog/', storage=upload_storage, default=settings.MEDIA_URL + '/img/flow.jpg')
    body = models.TextField()
    favorite = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    class Meta:
        ordering = ['posted', 'title']
