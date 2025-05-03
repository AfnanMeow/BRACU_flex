from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from module2.models import UploadedVideo ## Eikhane onek boro jhamel ase!!!
from module1.models import Video

def share_movie(request, token):
    video = get_object_or_404(Video, share_token=token) 
    share_url = request.build_absolute_uri(f"/share/{video.share_token}/")
    
    messages.success(request, f"Shareable Link: {share_url}")
    return render(request, "shared.html", {"Video" : video})  # Redirect to wherever you want (e.g., homepage)
