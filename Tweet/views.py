from django.shortcuts import render
from django.views.generic import DetailView
from .models import Tweet
def home(request):
	return render(request,'Tweet/home.html',{})


class TweetDetailView(DetailView):
	   template_name='Tweet/tweet_detail.html'
	   queryset=Tweet.objects.all()
     
