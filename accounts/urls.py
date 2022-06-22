from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('login/', views.signin, name='login'),
	path('register/', views.signup, name='signup'),

]