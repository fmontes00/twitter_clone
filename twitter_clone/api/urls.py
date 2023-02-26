from django.urls import path
from .views import TwitterList, TweetCreation, TweetRetriveDestroyUpdate, LikeList, LikeCreation, LikeUpdateRetriveDelete

urlpatterns = [
    path("", TwitterList.as_view(), name="tweets_list"),
    path("create-tweet/", TweetCreation.as_view(), name="tweet_creation"),
    path("retrive-update-delete/<int:pk>/", TweetRetriveDestroyUpdate.as_view(), name="tweet_up_del_re"),
    path("like-list/", LikeList.as_view(), name="like_list"),
    path("like-create/", LikeCreation.as_view(), name="like_create"),
    path("like-retrive-update-delete/<int:pk>/", LikeUpdateRetriveDelete.as_view(), name="like_up_del_re"),
]