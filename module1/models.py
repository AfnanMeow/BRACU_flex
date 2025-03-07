from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings

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

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ FIXED
    watching_hour = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
