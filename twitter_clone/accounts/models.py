from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):    
    is_premium = models.BooleanField(default=False)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Relationship(models.Model):
    user = models.ForeignKey("accounts.User", on_delete= models.CASCADE)
    follower = models.ForeignKey("accounts.User")
    following = models.ForeignKey("accounts.User")

