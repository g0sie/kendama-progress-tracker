from django.shortcuts import render

from .models import Trick, UserTrick


def user_tricks(request):
    """displays list of a user's tricks"""
    if request.user.is_authenticated:
        user_trick_pairs = UserTrick.objects.filter(user=request.user).select_related("trick")
        return render(request, "tricks/user_tricks.html", {'user_trick_pairs': user_trick_pairs})
