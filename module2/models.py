from django.conf import settings
from django.db import models

class UploadedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='uploads/')
    is_public = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title