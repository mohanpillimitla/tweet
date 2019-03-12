from django.urls import path
from .views import home,contactView,createForm

urlpatterns=[
               path('',home,name='home'),
               path('contact/',contactView,name='contact'),
               path('tweet',createForm,name='tweet'),








]