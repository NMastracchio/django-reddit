# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_selftext',
            field=models.TextField(default=b'Not a self post', max_length=40000, verbose_name=b'Self post text'),
        ),
    ]
