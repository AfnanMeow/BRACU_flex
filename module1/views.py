
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.http import HttpResponse
import requests
from django.contrib.auth import get_user_model, login
from django.contrib.auth.backends import ModelBackend
from django.http import JsonResponse
import json
from .models import Video, UserProfile, WatchProgress
from module2.models import UploadedVideo

Customer = get_user_model()

def index(request):
    return render(request, "index.html")

###############Login signup Module-01 ####################################
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ip_address = get_client_ip(request)  # Store IP
            user.save()

            # Explicitly setting the backend
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend  # Set backend explicitly

            login(request, user, backend=backend)  # Pass backend to login()
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def get_client_ip(request):
    """ Function to get client IP address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Get the first IP from the list
    else:
        ip = request.META.get('REMOTE_ADDR')  # Fallback to default method
    
    # If still localhost, get external IP using a request (only works in production)
    if ip == "127.0.0.1":
        import requests
        try:
            ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
        except Exception:
            ip = "Unknown"

    return ip


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        try:
            user = CustomUser.objects.get(username=email)
            print(user == None)
            auth_user = authenticate(username=user.username, password = password)
            print(user.password)
            if auth_user:
                login(self.request, auth_user)
                return redirect('home')
        except ObjectDoesNotExist:
            return HttpResponse("Invalid credentials", status=401)

def google_login(request):
    """ Redirect user to Google OAuth Login """
    return redirect('/oauth/login/google-oauth2/')

@login_required
def home(request):
    videos = Video.objects.all() 
    return render(request, 'home.html', {'user': request.user}, {"videos": videos})

def logout_view(request):
    logout(request)
    return redirect('login')




####################Login-signup Module 1 ends here ############################
def browse_database(request):
    return render(request, "search.html")

def profile_select(request):
    return render(request, "profile.html")


def show_details(request, serial_no):
    vid = get_object_or_404(Video, id=serial_no)
    return render(request, 'movie.html', {'video': vid})

def review(request, serial_no):
    vid = get_object_or_404(Video, id=serial_no)
    return render(request, 'review.html', {'video': vid}) 


@login_required
def home(request):
    videos = Video.objects.all()
    progress_data = WatchProgress.objects.filter(user=request.user)
    video_progress = {wp.video_id: wp.progress for wp in progress_data}

    return render(request, "home.html", {
        "videos": videos,
        "user": request.user,
        "video_progress": video_progress,
    })



def update_watch_time(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            watch_time = data.get("watch_time", 0)  # Get watch_time from request
            
            print(f"Received watch time: {watch_time} seconds")  #  Log watch time in console
            
            user = request.user
            if user.is_authenticated:
                # Convert seconds to minutes
                user.watching_hour = watch_time #in seconds sorryyyy  
                user.save(update_fields=["watching_hour"])  #  Update only watching_hour
                
                print(f"Updated user watching_hour: {user.watching_hour}")  # Log update
                
                return JsonResponse({"message": "Watch time updated!", "watching_hour": user.watching_hour})
            
        except json.JSONDecodeError:
            print("Invalid JSON received")  # Log JSON error
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)




@login_required
def update_video_progress(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            video_id = data.get("video_id")
            progress = data.get("progress")

            if video_id is None or progress is None:
                return JsonResponse({"error": "Missing data"}, status=400)

            video = Video.objects.get(id=video_id)

            # Update or create the progress
            watch_obj, created = WatchProgress.objects.update_or_create(
                user=request.user,
                video=video,
                defaults={"progress": progress}
            )

            return JsonResponse({"message": "Progress saved", "progress": watch_obj.progress})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)