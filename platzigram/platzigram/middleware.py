"""Platzigram meddleware"""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMilddleware:
    """Profile completion middleware"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [
                        reverse('update_profile'),
                        reverse('end'),
                    ]:
                        return redirect('update_profile')
        response = self.get_response(request)
        return response