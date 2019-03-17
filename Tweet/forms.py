from .models import UserTweet
from django import forms


class TweetCreateForm(forms.ModelForm):


	  class Meta:
	  	model=UserTweet
	  	fields=['title','content']


class TweetUpdateForm(forms.ModelForm):

      class Meta:
      	model=UserTweet
      	fields=['title','content']