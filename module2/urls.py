from django.urls import path
from .views import upload_video, my_uploads, public_videos, search_videos


from . import views #Afaf-Only

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('my-uploads/', my_uploads, name='my_uploads'),
    path('public/', public_videos, name='public_videos'),
    path('search/', search_videos, name='search_videos'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/add/<int:video_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<int:video_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('add_to_watchlist/<int:video_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('afaf/', views.movie_home, name='movie_home'),
    path('add-movie/', views.add_movie, name='add_movie'),
    path('update-movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('movie-list/', views.movie_list, name='movie_list'),
]
