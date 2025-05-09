from django.shortcuts import render, redirect
from .forms import UploadedVideoForm
from .models import UploadedVideo
from module1.models import Video  # import the main Video model
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from module1.models import Video
from .models import WatchlistItem

from .forms import MovieForm
from .models import Movie
from django.contrib.admin.views.decorators import staff_member_required



@login_required
def upload_video(request):
    if request.method == 'POST':
        form = UploadedVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()

            # Save to main Video model only if it's public
            if video.is_public:
                Video.objects.create(
                    title=video.title,
                    file=video.video_file  # same file is reused
                )

            return redirect('my_uploads')
    else:
        form = UploadedVideoForm()
    return render(request, 'upload_video.html', {'form': form})


@login_required
def my_uploads(request):
    videos = UploadedVideo.objects.filter(user=request.user)
    return render(request, 'my_uploads.html', {'videos': videos})


def public_videos(request):
    videos = UploadedVideo.objects.filter(is_public=True)
    return render(request, 'public_videos.html', {'videos': videos})


def search_videos(request):
    query = request.GET.get('q', '')
    videos = UploadedVideo.objects.filter(
        Q(title__icontains=query) | 
        Q(user__username__icontains=query) | 
        Q(video_file__icontains=query)  # Search in the file name
    ) if query else []
    return render(request, 'search_results.html', {'videos': videos, 'query': query})
@login_required
def add_to_watchlist(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    WatchlistItem.objects.get_or_create(user=request.user, video=video)
    return redirect('watchlist')  # Redirect to the watchlist page

@login_required
def remove_from_watchlist(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    WatchlistItem.objects.filter(user=request.user, video=video).delete()
    return redirect('watchlist')

@login_required
def watchlist(request):
    items = WatchlistItem.objects.filter(user=request.user).select_related('video')
    return render(request, 'watchlist.html', {'items': items})


@staff_member_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

@staff_member_required
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')  # Redirect to the movie list after updating
    else:
        form = MovieForm(instance=movie)
    return render(request, 'update_movie.html', {'form': form})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_home(request):
    movies = Movie.objects.all()  # Fetch all movies
    return render(request, 'movie_home.html', {'movies': movies})
