# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_auto_20161128_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='publish_presentations_to_dropbox',
            field=models.BooleanField(default=False),
        ),
    ]
