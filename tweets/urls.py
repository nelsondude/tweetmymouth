
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import TweetListView, TweetDetailView



urlpatterns = [

    url(r'^1/$', TweetDetailView.as_view(), name='detail'),
    url(r'^$', TweetListView.as_view(), name='list'),
]
