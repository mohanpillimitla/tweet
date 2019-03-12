from django.shortcuts import render,get_object_or_404,redirect
from .forms import TweetCreateForm
from .models import UserTweet
from django.contrib.auth.decorators import login_required
def home(request):
	return render(request,'Tweet/home.html',{})


def contactView(request):
	return render(request,'Tweet/contact.html',{})
@login_required
def createForm(request):
	if request.method=='POST':
		form=TweetCreateForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()


			return redirect('home')
	else:
		form=TweetCreateForm()
	context={'form':form}
	return render(request,'Tweet/createform.html',context)