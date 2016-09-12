from django.conf.urls import patterns, url
from twitter import views

urlpatterns = patterns("",
	url(r"^$", views.index, name="index"),
	url(r'^(?P<username>\w+)/$', views.followers, name="followers"),
	)