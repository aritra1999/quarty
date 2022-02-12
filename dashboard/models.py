from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from quarty.utils import slug_generator

POST_TYPE_CHOICES = (
    ("image", "Image"),
    ("blog", "Blog"),
    ("info", "Lead Info"),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=11, blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slug_generator()
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return self.user.username
