# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('file_link', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.FileField(default='https://.s3.amazonaws.com/media//img/flow.jpg', storage=info.models.MediaS3BotoStorage(), upload_to='file/blog/')),
                ('body', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
                ('gplay', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhoIAm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
