from django.db import models

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    coment_of = models.OneToOneField(self, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)