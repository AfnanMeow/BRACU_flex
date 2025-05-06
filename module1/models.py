from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.utils import timezone



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

# module1/models.py

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles')
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    age_limit = models.CharField(max_length=10, choices=[('All', 'All'), ('Kids', 'Kids')], default='All')

    created_at = models.DateTimeField(auto_now_add=True)

    watching_hour = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class WatchProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)  # in seconds
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'video')  # prevent duplicate entries per video/user pair

    def __str__(self):
        return f"{self.user.username} - {self.video.title} - {self.progress}s"
    



from django.db import models
from django.conf import settings

class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    name = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    download_limit = models.IntegerField(
        null=True, blank=True, help_text="Download limit in GB. Null = unlimited."
    )
    has_enhanced_support = models.BooleanField(default=False)
    has_enhanced_catalog = models.BooleanField(default=False)

    def __str__(self):
        return self.get_name_display()

class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"

    

class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"




class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('card', 'Card'),
    ]

    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Update this line
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for {self.user.username} - {self.status}"
