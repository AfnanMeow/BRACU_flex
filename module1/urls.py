from django.urls import path
from .views import signup, CustomLoginView, home, logout_view, google_login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import home, update_watch_time

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('google-login/', google_login, name='google_login'),
    path('', home, name='home'),
    path("update-watch-time/", update_watch_time, name="update-watch-time"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
