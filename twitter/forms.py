from django import forms
# from twitter.models import Followers

# class FollowersForm(forms.ModelForm):
	# name = forms.CharField(max_length=128, help_text="Get follower list of:")
	# class Meta:
		# model = Followers
		
class FollowersForm(forms.Form):
	user_name = forms.CharField(help_text="Get follower list of:", max_length=100)