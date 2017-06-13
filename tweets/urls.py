
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView



urlpatterns = [
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
]
