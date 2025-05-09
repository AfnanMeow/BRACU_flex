from module1.models import UserProfile

class ActiveProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        profile_id = request.session.get('active_profile_id')
        if request.user.is_authenticated and profile_id:
            try:
                request.active_profile = UserProfile.objects.get(id=profile_id, user=request.user)
            except UserProfile.DoesNotExist:
                request.active_profile = None
        else:
            request.active_profile = None

        return self.get_response(request)