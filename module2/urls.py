from django.urls import path
from .views import upload_video, my_uploads, public_videos

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('my-uploads/', my_uploads, name='my_uploads'),
    path('public/', public_videos, name='public_videos'),
]
