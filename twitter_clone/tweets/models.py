from django.db import models

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    coment = models.ForeignKey('Tweet', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Like(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)