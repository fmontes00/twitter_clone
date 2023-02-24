from dataclasses import field, fields
from rest_framework import serializers
from tweets.models import Tweet, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ("user", "content", "created")

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user", "tweet")