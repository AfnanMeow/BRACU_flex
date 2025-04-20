from django.urls import path
from .views import index, signup, CustomLoginView, home, browse_database, profile_select, logout_view, google_login,show_details, review, update_watch_time, update_video_progress
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import profile
 

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('google-login/', google_login, name='google_login'),
    path('home/', home, name='home'),
    path('browse_movies/', browse_database, name='browse_database'),
    path('movies/<str:serial_no>/', show_details, name='show_details'),
    path('movies/reviews/<str:serial_no>/', review, name='review'),
    path('choose_profiles/', profile_select, name='profile_select'),
    path('update-video-progress/', update_video_progress, name='update_video_progress'),
    path("update-watch-time/", update_watch_time, name="update-watch-time"),
    path('profile/', profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
