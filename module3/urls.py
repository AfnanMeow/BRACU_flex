
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_home, name='review_home'),
    path('movie/<int:movie_id>/add-review/', views.add_review, name='add_review'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('friends_viewed_content/', views.friends_viewed_content, name='friends_viewed_content'),
    path('show_friends/', views.show_friends, name='show_friends'),
]