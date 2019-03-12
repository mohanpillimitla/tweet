from django.db import models

from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class UserTweet(models.Model):
	  author=models.ForeignKey(User,on_delete=models.CASCADE)
	  title=models.CharField(max_length=10)
	  content=models.TextField()
	  updated=models.DateTimeField(auto_now=True)
	  timestamp=models.DateTimeField(auto_now_add=True)
	  def __str__(self):
	  	  return str(self.title)

	  