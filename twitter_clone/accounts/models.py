from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):    
    is_premium = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True) # check for upload_to

    def __str__(self):
        return self.username


class Relationship(models.Model):
    follower = models.ForeignKey("accounts.User" ,on_delete=models.CASCADE)
    following = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="+")

