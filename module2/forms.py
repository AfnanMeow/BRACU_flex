# forms.py
from django import forms
from .models import UploadedVideo

class UploadedVideoForm(forms.ModelForm):
    class Meta:
        model = UploadedVideo
        fields = ['title', 'video_file', 'is_public']