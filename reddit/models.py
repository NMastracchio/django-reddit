from django.db import models
from datetime import datetime

class Post(models.Model):
	def __unicode__(self):
		return self.post_title
	id = models.CharField(
		verbose_name='Post ID',
		primary_key=True,
		max_length=200
	)
	post_title = models.CharField(
		verbose_name='Post title',
		max_length=200
	)
	post_submitted_on = models.DateTimeField(
		verbose_name='Submitted on',
		null=True
	)
	post_upvotes = models.IntegerField(
		verbose_name='Upvotes',
		null=True
	)
	post_downvotes = models.IntegerField(
		verbose_name='Downvotes',
		null=True
	)
	post_score = models.IntegerField(
		verbose_name='Score',
		null=True
	)
	post_submitter = models.CharField(
		verbose_name='Submitted by',
		null=True,
		max_length=15
	)
	post_subreddit_id = models.CharField(
		verbose_name='Subreddit ID',
		null=True,
		max_length=200
	)
	post_comment_count = models.IntegerField(
		verbose_name='Number of comments', 
		null=True
	)
	post_permalink = models.URLField(
		verbose_name='Permalink',
		null=True
	)
	post_url = models.URLField(
		verbose_name='Post URL',
		null=True
	)
	post_subreddit = models.CharField(
		verbose_name='Subreddit',
		null=True,
		max_length=200
	)
	post_thumbnail = models.URLField(
		verbose_name='Thumbnail URL',
		null=True
	)
	post_selftext = models.TextField(
		verbose_name='Self post text',
		max_length=40000,
		default='Not a self post'
	)
	#post_comments = models.ForeignKey('Comment')

class Comment(models.Model):
	def __unicode__(self):
		return self.comment_body
	comment_user=models.CharField(max_length=200)
	comment_body=models.CharField(max_length=1024)