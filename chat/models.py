from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.CharField(max_length=1000, null=True, blank=True)
    message_from = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE)
    message_to = models.ForeignKey(User, related_name='message_to', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)

