import praw
import pprint
from django.http import HttpResponse
from django.views import generic
from datetime import datetime
import pytz
from .models import Post

local_tz = pytz.timezone("America/Los_Angeles")
user_agent = "osx:django/reddit:v1.0.1 (by /u/thestrachs)"
thing_limit = 10

class IndexView(generic.ListView):
	template_name = 'reddit/index.html'
	context_object_name = 'top_posts'

	#Get top 10 posts from the front page
	pp = pprint.PrettyPrinter(indent = 4)
	r = praw.Reddit(user_agent = user_agent)
	front_page = r.get_front_page(limit = thing_limit)
	for thing in front_page:
		# Format timestamp
		utc_dt = datetime.utcfromtimestamp(thing.created_utc).replace(
			tzinfo=pytz.utc
		)
		local_dt = local_tz.normalize(utc_dt.astimezone(local_tz))
		post = Post(
			id = thing.id,
			post_title = thing.title, 
			post_submitted_on = local_dt,
			post_upvotes = thing.ups,
			post_downvotes = thing.downs,
			post_score = thing.score,
			post_submitter = thing.author,
			post_comment_count = thing.num_comments,
			post_permalink = thing.permalink,
			post_url = thing.url,
			post_subreddit = thing.subreddit,
			post_subreddit_id = thing.subreddit_id,
			post_thumbnail = thing.thumbnail,
		)
		if thing.is_self:
			post.post_selftext = thing.selftext
		post.save()

	def get_queryset(self):
		# Return top 10 stories, in descending order by score
		return Post.objects.all().order_by('-post_score')[:10]

class PostView(generic.DetailView):
	model = Post
	template_name = 'reddit/post.html'

def post(request, post_id):
	return HttpResponse("You're looking at post %s." % post_id)