
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView
from .views import (
    TweetListAPIView,
    TweetCreateAPIView,
    RetweetAPIView,
    LikeToggleAPIView,
    )


urlpatterns = [
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/like$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^(?P<pk>\d+)/retweet$', RetweetAPIView.as_view(), name='retweet'),
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^$', RedirectView.as_view(url="/")),
]
