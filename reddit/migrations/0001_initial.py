# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_user', models.CharField(max_length=200)),
                ('comment_body', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=200, serialize=False, verbose_name=b'Post ID', primary_key=True)),
                ('post_title', models.CharField(max_length=200, verbose_name=b'Post title')),
                ('post_submitted_on', models.DateTimeField(null=True, verbose_name=b'Submitted on')),
                ('post_upvotes', models.IntegerField(null=True, verbose_name=b'Upvotes')),
                ('post_downvotes', models.IntegerField(null=True, verbose_name=b'Downvotes')),
                ('post_score', models.IntegerField(null=True, verbose_name=b'Score')),
                ('post_submitter', models.CharField(max_length=15, null=True, verbose_name=b'Submitted by')),
                ('post_subreddit_id', models.CharField(max_length=200, null=True, verbose_name=b'Subreddit ID')),
                ('post_comment_count', models.IntegerField(null=True, verbose_name=b'Number of comments')),
                ('post_permalink', models.URLField(null=True, verbose_name=b'Permalink')),
                ('post_url', models.URLField(null=True, verbose_name=b'Post URL')),
                ('post_subreddit', models.CharField(max_length=200, null=True, verbose_name=b'Subreddit')),
                ('post_thumbnail', models.URLField(null=True, verbose_name=b'Thumbnail URL')),
            ],
        ),
    ]
