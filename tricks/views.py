from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Trick, UserTrick


def user_tricks(request):
    """displays list of a user's tricks"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            # if user clicked '+1' button
            land_keys = [key for key in request.POST.keys() if key.startswith("land_")]
            if land_keys:
                key = int(land_keys[0].split("_")[1])
                land_trick(key)
            # if user clicked 'rank up' button
            rank_up_keys = [key for key in request.POST.keys() if key.startswith("rankup_")]
            if rank_up_keys:
                key = int(rank_up_keys[0].split("_")[1])
                rank_up_trick(key)
            return HttpResponseRedirect(reverse('tricks:user_tricks'))
        user_trick_pairs = UserTrick.objects.filter(user=request.user)\
            .select_related("trick").prefetch_related("trick__tutorials")
        return render(request, "tricks/user_tricks.html", {'user_trick_pairs': user_trick_pairs})


def land_trick(user_trick_id: int):
    user_trick = UserTrick.objects.get(id=user_trick_id)
    if user_trick.land_count <= 100:
        user_trick.land_count += 1
        user_trick.save()


def rank_up_trick(user_trick_id: int):
    user_trick = UserTrick.objects.get(id=user_trick_id)
    user_trick.rank += 1
    user_trick.save()
