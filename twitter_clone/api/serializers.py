from dataclasses import field, fields
from rest_framework import serializers
from tweets.models import Tweet, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ("id","user", "content", "created", "comment")

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id","user", "tweet")