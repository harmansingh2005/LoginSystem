from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup', views.signup, name='signup'),
   path('login', views.mylogin, name='mylogin'),
    path('logout', views.logout, name='logout'),
]