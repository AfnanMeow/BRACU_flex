from django.urls import path
from .views import share_movie
urlpatterns = [
    path('/share/<uuid:token>/', share_movie, name='share_movie'),
]