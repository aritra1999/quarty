from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User

POST_TYPE_CHOICES =(
    ("image", "Image"),
    ("blog", "Blog"),
    ("info", "Lead Info"),
)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)
