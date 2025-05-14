from django.shortcuts import render, redirect, get_object_or_404
from module2.models import UploadedVideo
from module1.models import Video




from .forms import ReviewForm
from .models import Review
from module2.models import Movie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Friendship, ViewedContent
from django.http import HttpResponse, HttpRequest
from .forms import AddFriendForm
from django.conf import settings
from django.contrib.auth import get_user_model



def shared_video(request, token):
    #video = get_object_or_404(UploadedVideo, share_token=token)
    video = get_object_or_404(Video, share_token=token)
    print(video.title, video.share_token, "Mewaaaaaaaa")
    shareable_url = request.build_absolute_uri()  # Gets full URL

    return render(request, 'shared_video.html', {
        'video': video,
        'shareable_url': shareable_url
    })



#Afaf-Only

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})

def review_home(request):
    movies = Movie.objects.all()  # Fetch all movies
    return render(request, 'review_home.html', {'movies': movies})







User = get_user_model()  # Use the custom user model

def add_friend(request):
    if request.method == 'POST':
        form = AddFriendForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            friend = get_object_or_404(User, username=username)  # Query the custom user model
            if not Friendship.objects.filter(user=request.user, friend=friend).exists():
                Friendship.objects.create(user=request.user, friend=friend)
                return render(request, 'add_friend.html', {'form': form, 'message': 'Friend added successfully!'})
            else:
                return render(request, 'add_friend.html', {'form': form, 'message': 'Friend already added!'})
    else:
        form = AddFriendForm()
    return render(request, 'add_friend.html', {'form': form})


def friends_viewed_content(request):
    friends = Friendship.objects.filter(user=request.user).values_list('friend', flat=True)
    content = ViewedContent.objects.filter(user__id__in=friends).order_by('-viewed_at')
    return render(request, 'friends_viewed_content.html', {'content': content})

def show_friends(request):
    friends = Friendship.objects.filter(user=request.user).select_related('friend')
    return render(request, 'show_friends.html', {'friends': friends})
