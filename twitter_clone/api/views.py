from django.shortcuts import render
from rest_framework import generics
from tweets.models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer 
from .permissions import IsAuthorOrReadOnly



class TwitterList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TweetSerializer

class TweetCreation(generics.CreateAPIView):
    queryset = Tweet
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TweetSerializer

class TweetRetriveDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TweetSerializer


class LikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer

class LikeCreation(generics.CreateAPIView):
    queryset = Like
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer

class LikeUpdateRetriveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer





