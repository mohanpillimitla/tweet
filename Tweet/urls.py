from django.urls import path
from .views import home,TweetDetailView

urlpatterns = [
    path('',home,name='home'),
    path('tweet/<int:pk>/',TweetDetailView.as_view(),name='tweet'),
]