from django.urls import path
from . import views

urlpatterns = [
    
    path('shared/<uuid:token>/', views.shared_video, name='shared_video'),
]