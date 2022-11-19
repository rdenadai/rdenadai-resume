from __future__ import unicode_literals

from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)
from django.utils.deconstruct import deconstructible

"""Custom S3 storage backends to store files in subfolders."""
from storages.backends.s3boto import S3BotoStorage

from resume import settings


@deconstructible
class MediaS3BotoStorage(S3BotoStorage):
    location: str = "media"


class Category(Model):
    name: CharField = CharField(max_length=255)
    slug: SlugField = SlugField(max_length=100, db_index=True)
    posted: DateField = DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return ("view_blog_category", None, {"slug": self.slug})

    class Meta:
        ordering = ["name"]


class Blog(Model):
    upload_storage: MediaS3BotoStorage = MediaS3BotoStorage()

    title: CharField = CharField(max_length=100, unique=True)
    slug: SlugField = SlugField(max_length=100, unique=True)
    description: TextField = TextField(max_length=255, null=True)
    image: ImageField = ImageField(
        upload_to="img/blog/",
        storage=upload_storage,
        default=settings.MEDIA_URL + "img/flow.jpg",
    )
    body: TextField = TextField()
    favorite: IntegerField = IntegerField(default=0)
    published: BooleanField = BooleanField(default=False)
    category: ManyToManyField = ManyToManyField(Category)
    posted: DateField = DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return ("view_blog_post", None, {"slug": self.slug})

    class Meta:
        ordering: list = ["posted", "title"]
