from django.urls import path
from .views import signup, CustomLoginView, home, logout_view, google_login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import home, update_watch_time
from django.urls import path
from . import views
from .views import signup, CustomLoginView, home, logout_view, google_login
from module2.views import movie_home, add_movie, update_movie
from module3.views import show_friends as show_added_friends, review_home


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('google-login/', google_login, name='google_login'),
    path('', home, name='home'),
    path('movie_home/', movie_home, name='movie_home'),
    path('add_movie/', add_movie, name='add_movie'),
    path('edit_movie/<int:movie_id>/', update_movie, name='edit_movie'),
    path('show_added_friends/', show_added_friends, name='show_added_friends'),
    path('review_home/', review_home, name='review_home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
