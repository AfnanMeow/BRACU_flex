from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
import uuid

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    watching_hour = models.PositiveIntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="videos/")
    share_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    watching_hour = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class WatchProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)  # in seconds
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'video')  # prevent duplicate entries per video/user pair

    def __str__(self):
        return f"{self.user.username} - {self.video.title} - {self.progress}s"