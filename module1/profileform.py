from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Age'
    }))
    watching_hour = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Watching Hours'
    }))
    ip_address = forms.GenericIPAddressField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'IP Address'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'age', 'watching_hour', 'ip_address']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old Password'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }))
