from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follwer = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    interests = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)