#This gives us access to the url function
from django.conf.urls import url
#This explicitly imports views.py in the current folder
from . import views
urlpatterns = [
    url(r'^$', views.index),

]
