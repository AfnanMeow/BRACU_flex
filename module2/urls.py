from django.urls import path
from .views import upload_video, my_uploads, public_videos
from . import views

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('my-uploads/', my_uploads, name='my_uploads'),
    path('public/', public_videos, name='public_videos'),
]


urlpatterns = [
    path('', views.movie_home, name='movie_home'),
    path('add-movie/', views.add_movie, name='add_movie'),
    path('update-movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('movie-list/', views.movie_list, name='movie_list'),
]