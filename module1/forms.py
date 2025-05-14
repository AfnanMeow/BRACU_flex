from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from .models import UserProfile

class SignUpForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'age']

# module1/forms.py



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'avatar', 'age_limit']
