from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):    
    is_premium = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username


class Relationship(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    follower = models.ForeignKey(CustomUser)
    following = models.ForeignKey(CustomUser)

