from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SubscriptionPlan, UserSubscription


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    watching_hour = models.PositiveIntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="videos/")

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ FIXED
    watching_hour = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class WatchProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)  # in seconds
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'video')  # prevent duplicate entries per video/user pair

    def __str__(self):
        return f"{self.user.username} - {self.video.title} - {self.progress}s"
    
class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    
    name = models.CharField(max_length=20, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    download_limit = models.IntegerField(null=True, blank=True, help_text="Download limit in GB. Null means unlimited.")
    has_enhanced_support = models.BooleanField(default=False)
    has_enhanced_catalog = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
    
@property
def subscription_plan(self):
    try:
        return self.subscription.plan
    except:
        return None