# Generated by Django 2.2.2 on 2019-06-13 17:57

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='file',
            field=models.FileField(default='/media//img/flow.jpg', storage=info.models.MediaS3BotoStorage(), upload_to='file/blog/'),
        ),
    ]
