from django.shortcuts import render
from rest_framework import generics
from tweets.models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer 



class TwitterList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class TweetCreation(generics.CreateAPIView):
    queryset = Tweet
    serializer_class = TweetSerializer

class TweetRetriveDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet
    serializer_class = TweetSerializer


class LikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeCreation(generics.CreateAPIView):
    queryset = Like
    serializer_class = LikeSerializer

class LikeUpdateRetriveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like
    serializer_class = LikeSerializer





