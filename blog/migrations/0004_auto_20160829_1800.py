# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-29 22:00
from __future__ import unicode_literals

from django.db import migrations
from blog import models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160826_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.HTMLField(),
        ),
    ]
