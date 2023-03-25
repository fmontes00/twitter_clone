from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LikeList, LikeCreation, LikeUpdateRetriveDelete, TweetViewSet             # TwitterList, TweetCreation, TweetRetriveDestroyUpdate,  


router = DefaultRouter(trailing_slash=False)
router.register(r"tweets", TweetViewSet, basename="tweet")

urlpatterns = [
    #path("", TwitterList.as_view(), name="tweets_list"),
    #path("create-tweet/", TweetCreation.as_view(), name="tweet_creation"),
    #path("retrive-update-delete/<int:pk>/", TweetRetriveDestroyUpdate.as_view(), name="tweet_up_del_re"),
    path("",include(router.urls)),
    path("like-list/", LikeList.as_view(), name="like_list"),
    path("like-create/", LikeCreation.as_view(), name="like_create"),
    path("like-retrive-update-delete/<int:pk>/", LikeUpdateRetriveDelete.as_view(), name="like_up_del_re"),
    
]