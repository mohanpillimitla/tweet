from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	  user=models.OneToOneField(User,on_delete=models.CASCADE)
	  firstname=models.CharField(max_length=20)
	  lastname=models.CharField(max_length=20)
	  branch=models.CharField(max_length=30)
	  year_of_study=models.CharField(max_length=1)
	  collegename=models.CharField(max_length=40)
	  college_location=models.CharField(max_length=20)
	  mobileno=models.CharField(max_length=10,help_text='enter your mobile number')
	  email_verified=models.BooleanField(default=False)
	  def __str__(self):
	  	  return f'{self.user.username} profile'



	  