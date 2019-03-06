from django.shortcuts import render
def home(request):
	return render(request,'Tweet/home.html',{})


def contactView(request):
	return render(request,'Tweet/contact.html',{})