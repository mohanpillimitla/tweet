from django.shortcuts import render,get_object_or_404,redirect
from .forms import TweetCreateForm,TweetUpdateForm
from .models import UserTweet
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def home(request):
	queryset=UserTweet.objects.all()
	context={'object_list':queryset}
	return render(request,'Tweet/home.html',context)


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


def detailView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	return render(request,'Tweet/detailview.html',context)


@login_required
def deleteView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	if request.method=='POST' and request.user==obj.author:
		obj.delete()
		messages.success(request,f'post deleted successfully')
		return redirect('home')
	else:
		if request.user!=obj.author:
			messages.error(request,f'you are not allowed to delete this !!!')
	
		return render(request,'Tweet/deleteform.html',context)


@login_required
def TweetUpdateView(request,id):
	obj=get_object_or_404(UserTweet,id=id)
	context={'object':obj}
	form=TweetUpdateForm(request.POST or None,instance=obj)
	if request.method=='POST' and request.user==obj.author:
	            form=TweetUpdateForm(request.POST or None,instance=obj)

	            if form.is_valid():
	   	          form.save()
	   	          return render(request,'Tweet/detailview.html',context)


	else:
		if request.user!=obj.author:
			messages.error(request,f'you are not allowed to edit this !!!')
	
		form=TweetUpdateForm(instance=obj)
		context={'form':form}
		return render(request,'Tweet/createform.html',context)
