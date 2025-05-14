from django.conf import settings
from django.db import models
import os, uuid


from module1.models import Video #Afaf-Only

def video_upload_path(instance, filename):
    # Choose folder based on is_public value
    folder = 'uploads' if instance.is_public else 'uploads/private'
    return os.path.join(folder, filename)






class UploadedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to=video_upload_path)
    is_public = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    share_token = models.UUIDField(unique=True, default=uuid.uuid4)





class WatchlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey('module1.Video', on_delete=models.CASCADE)  
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"
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
