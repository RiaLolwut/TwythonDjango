from django.db import models

class Followers(models.Model):
	name = models.CharField(max_length=128)
	def __unicode__(self):
		return self.name