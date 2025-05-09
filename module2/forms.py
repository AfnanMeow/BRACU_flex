# forms.py
from django import forms
from .models import UploadedVideo
from .models import Movie #Afaf-Only

class UploadedVideoForm(forms.ModelForm):
    class Meta:
        model = UploadedVideo
        fields = ['title', 'video_file', 'is_public']
        

#Afaf-Only
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'release_date']
