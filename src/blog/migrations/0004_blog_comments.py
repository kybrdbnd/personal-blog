# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 13:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20170611_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='blog_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]