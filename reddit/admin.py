from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				 {'fields':['post_title']}),
		('Post Information', {'fields':[
			'id',
			'post_submitted_on',
			'post_submitter',
			'post_subreddit_id',
			'post_upvotes',
			'post_downvotes',
			'post_score',
			'post_comment_count',
			'post_permalink',
			'post_url',
			'post_subreddit',
			'post_thumbnail',
			'post_selftext',
		]}),
	]
	readonly_fields = (
		'id',
		'post_title',
		'post_submitted_on',
		'post_upvotes',
		'post_downvotes',
		'post_score',
		'post_submitter',
		'post_comment_count',
		'post_subreddit_id',
		'post_subreddit',
		'post_selftext'
	)
admin.site.register(Post, PostAdmin)
