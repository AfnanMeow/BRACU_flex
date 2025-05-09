# forms.py
from django import forms
from .models import UploadedVideo
from .models import Movie

class UploadedVideoForm(forms.ModelForm):
    class Meta:
        model = UploadedVideo
        fields = ['title', 'video_file', 'is_public']
        


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'release_date']