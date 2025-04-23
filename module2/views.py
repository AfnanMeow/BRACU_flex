from django.shortcuts import render, redirect
from .forms import UploadedVideoForm
from .models import UploadedVideo
from module1.models import Video  # import the main Video model
from django.contrib.auth.decorators import login_required



@login_required
def upload_video(request):
    if request.method == 'POST':
        form = UploadedVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()

            # Save to main Video model only if it's public
            if video.is_public:
                Video.objects.create(
                    title=video.title,
                    file=video.video_file  # same file is reused
                )

            return redirect('my_uploads')
    else:
        form = UploadedVideoForm()
    return render(request, 'upload_video.html', {'form': form})

@login_required
def my_uploads(request):
    videos = UploadedVideo.objects.filter(user=request.user)
    return render(request, 'my_uploads.html', {'videos': videos})

def public_videos(request):
    videos = UploadedVideo.objects.filter(is_public=True)
    return render(request, 'public_videos.html', {'videos': videos})



