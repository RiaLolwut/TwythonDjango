from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from twitter.forms import FollowersForm
import datetime
import csv
import re
from twython import Twython, TwythonError

TWITTER_KEY = ""
TWITTER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

def index(request):
	context = RequestContext(request)
	if request.method == "POST":
		form = FollowersForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data["user_name"]
			return HttpResponseRedirect(username)
		else:
			print form.errors
	else:
		form = FollowersForm()
	return render_to_response("twitter/index.html", {"form": form}, context)

def followers(request,username):
	context = RequestContext(request)
	datestamp = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")
	names = []
	usernames = []
	ids = []
	locations = []
	follower_count = []
	next_cursor = -1
	error = ""
	form = ""
	user_pic = ""
	user_name = ""
	user_username = ""
	user_desc = ""
	user_id = ""
	user_age = ""
	user_following = ""
	user_location = ""
	user_status = ""
	num_users = 0
	twitter = Twython(TWITTER_KEY, TWITTER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	while(next_cursor):
		if request.method == "POST":
			form = FollowersForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				username = data["user_name"]
				return HttpResponseRedirect(username)
			else:
				print form.errors
		else:
			form = FollowersForm()
		try:
			user_pic = re.sub("(_normal)", "", twitter.show_user(screen_name=username)["profile_image_url"])
			user_name = twitter.show_user(screen_name=username)["name"].encode("utf-8")
			user_username = twitter.show_user(screen_name=username)["screen_name"].encode("utf-8")
			user_desc = twitter.show_user(screen_name=username)["description"].encode("utf-8")
			user_id = twitter.show_user(screen_name=username)["id"]
			user_age = twitter.show_user(screen_name=username)["created_at"]
			user_following = twitter.show_user(screen_name=username)["friends_count"]
			user_location = twitter.show_user(screen_name=username)["location"].encode("utf-8")
			user_status = twitter.show_user(screen_name=username)["status"]["text"].encode("utf-8")
			get_followers = twitter.get_followers_list(screen_name=username, count=200, cursor=next_cursor)
			for follower in get_followers["users"]:
				names.append(follower["name"].encode("utf-8"))
				usernames.append(follower["screen_name"].encode("utf-8"))
				ids.append(follower["id"])
				locations.append(follower["location"].encode("utf-8"))
				follower_count.append(follower["followers_count"])
				next_cursor = get_followers["next_cursor"]
				num_users = len(names)
		except TwythonError as e:
			error = "The user @%s cannot be found. \n%s" % (username, e)
			break
	context_dict = {
		"username": username,
		"user_pic": user_pic,
		"error": error,
		"datestamp": datestamp,
		"followers": followers,
		"num_users": str(num_users),
		"rows": zip(names,usernames,ids,locations,follower_count),
		"form": form,
		"user_name": user_name,
		"user_username": user_username,
		"user_desc": user_desc,
		"user_id": user_id,
		"user_age": user_age,
		"user_following": user_following,
		"user_location": user_location,
		"user_status": user_status,
		}
	return render_to_response("twitter/followers.html", context_dict, context)
