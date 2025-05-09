from django import forms
from .models import Review
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class AddFriendForm(forms.Form):
    username = forms.CharField(max_length=150, label="Friend's Username")