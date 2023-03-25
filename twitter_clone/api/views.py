from django.shortcuts import render
from rest_framework import generics, viewsets, status
from tweets.models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer 
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly


"""
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

"""
class LikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer

class LikeCreation(generics.CreateAPIView):
    queryset = Like
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer

class LikeUpdateRetriveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = LikeSerializer



class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = TweetSerializer



# class TweetViewSet(viewsets.ViewSet):

#     permission_classes = (IsAuthorOrReadOnly,)

#     def list(self, request):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)


#     def create(self, request):
#         serializer = TweetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(
#             {"detail": "Given payload is invalid"}, status=status.HTTP_400_BAD_REQUEST
#         )


#     def retrieve(self, request, pk=None):
#         try:
#             tweet = Tweet.objects.get(id=pk)
#         except Tweet.DoesNotExist:
#             return Response(
#                 {"detail": "Tweet not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)
    

#     def update(self, request, pk=None):
#         try:
#             tweet = Tweet.objects.get(id=pk)
#         except Tweet.DoesNotExist:
#             return Response(
#                 {"detail": "Tweet not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = TweetSerializer(tweet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#         def destroy(self, request, pk=None):
#             try:
#                 tweet = Tweet.objects.get(id=pk)
#             except Tweet.DoesNotExist:
#                 return Response(
#                     {"detail": "Tweet not found"}, status=status.HTTP_404_NOT_FOUND
#                 )
#             tweet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
        


#         def partial_update(self, request, pk=None):
#             try:
#                 tweet = Tweet.objects.get(id=pk)
#             except Tweet.DoesNotExist:
#                 return Response(
#                     {"detail": "Tweet not found"}, status=status.HTTP_404_NOT_FOUND
#                 )
#             serializer = TweetSerializer(tweet, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    






