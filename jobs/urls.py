from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

path('', views.jobs, name='jobs'),
path('post-job/', views.postjob, name='postjob'),

]