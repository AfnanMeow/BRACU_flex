from django.conf import settings
from django.db import models
<<<<<<< Updated upstream
=======
import os, uuid


def video_upload_path(instance, filename):
    # Choose folder based on is_public value
    folder = 'uploads' if instance.is_public else 'uploads/private'
    return os.path.join(folder, filename)

>>>>>>> Stashed changes

class UploadedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='uploads/')
    is_public = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    share_token = models.UUIDField(default=uuid.uuid4, unique=True)