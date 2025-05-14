from django.urls import path
from .views import index, signup, CustomLoginView, home, browse_database, profile_select, logout_view, google_login,show_details, review, update_watch_time, update_video_progress, create_profile, set_active_profile, delete_profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import profile
from module1 import views
from django.urls import path
from .views import profile_select, create_profile, set_active_profile, delete_profile



 
#Afaf-only
from . import views
from .views import signup, CustomLoginView, home, logout_view, google_login
from module2.views import movie_home, add_movie, update_movie
from module3.views import show_friends as show_added_friends, review_home


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
    path("subscription/", views.subscription_page, name="subscription"),
    path('profiles/', profile_select, name='profile_select'),
    path('profiles/create/', create_profile, name='create_profile'),
    path('profiles/select/<int:profile_id>/', set_active_profile, name='set_active_profile'),
    path('profiles/delete/<int:profile_id>/', delete_profile, name='delete_profile'),
    path('subscription/checkout/<int:plan_id>/', views.checkout, name='checkout'),
    path('checkout/<int:plan_id>/', views.checkout, name='checkout'),

    #afaf-only
    path('movie_home/', movie_home, name='movie_home'),
    path('add_movie/', add_movie, name='add_movie'),
    path('edit_movie/<int:movie_id>/', update_movie, name='edit_movie'),
    path('show_added_friends/', show_added_friends, name='show_added_friends'),
    path('review_home/', review_home, name='review_home'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
