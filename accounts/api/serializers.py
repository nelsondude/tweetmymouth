from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# from tweets.models import Tweet


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url'
            # 'email',

        ]

    def get_follower_count(self, obj):
        # print(obj.username)
        return 0

    def get_url(self, obj):
        return reverse_lazy("profiles:detail", kwargs={"username": obj.username})