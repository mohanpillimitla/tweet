from django.urls import path
from .views import home,contactView,createForm,detailView,deleteView,TweetUpdateView

urlpatterns=[
               path('',home,name='home'),
               path('contact/',contactView,name='contact'),
               path('tweet',createForm,name='tweet'),
               path('tweet/<int:id>/',detailView,name='detail'),
               path('tweet/<int:id>/update/',TweetUpdateView,name='update'),

               path('tweet/<int:id>/delete/',deleteView,name='delete'),
              









]