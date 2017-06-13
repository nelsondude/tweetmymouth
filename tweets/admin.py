from django.contrib import admin

# Register your models here.

from .models import Tweet

class TweetAdmin(admin.ModelAdmin):

    class Meta:
        model = Tweet
        fields = [
            'id',
            'content'
        ]

admin.site.register(Tweet)