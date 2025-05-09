from django.shortcuts import get_object_or_404, render
from module2.models import UploadedVideo
from module1.models import Video

def shared_video(request, token):
    #video = get_object_or_404(UploadedVideo, share_token=token)
    video = get_object_or_404(Video, share_token=token)
    print(video.title, video.share_token, "kuttaaaaaaaa")
    return render(request, 'shared_video.html', {'video': video})