from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Trick, UserTrick
from .forms import TrickForm


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
        user_trick_pairs = UserTrick.objects.filter(user=request.user) \
            .select_related("trick").prefetch_related("trick__tutorials") \
            .order_by("rank", "-trick__official")
        return render(request, "tricks/user_tricks.html", {'user_trick_pairs': user_trick_pairs})


def land_trick(user_trick_id: int):
    user_trick = UserTrick.objects.get(id=user_trick_id)
    if user_trick.land_count <= 100:
        user_trick.land_count += 1
        user_trick.save()


def rank_up_trick(user_trick_id: int):
    requirements = {
        1: 10,
        2: 25,
        3: 50,
        4: 100,
        5: 999,
    }
    user_trick = UserTrick.objects.get(id=user_trick_id)
    if user_trick.land_count >= requirements[user_trick.rank]:
        user_trick.rank += 1
        user_trick.save()


def add_new_trick(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TrickForm(data=request.POST)
            if form.is_valid():
                trick = form.save()
                UserTrick.objects.create(user=request.user, trick=trick)
                HttpResponseRedirect(reverse("tricks:add_new_trick"))
        form = TrickForm()
        return render(request, 'tricks/add_new_trick.html', {'form': form})
      
      
def add_from_list(request):
    """displays official trick list"""
    if request.user.is_authenticated:
        if request.method == "POST":
            # get id of the trick to add
            add_keys = [key for key in request.POST.keys() if key.startswith("add_")]
            add_key = int(add_keys[0].split("_")[1])
            # check if user has the trick already
            if add_key not in UserTrick.objects.filter(user=request.user).values("trick__id"):
                trick = Trick.objects.get(id=add_key)
                UserTrick.objects.create(user=request.user, trick=trick)
        # display only the tricks the user doesn't have
        user_tricks_ids = UserTrick.objects.filter(user=request.user).values('trick__id')
        tricks = Trick.objects.filter(official=True).exclude(id__in=user_tricks_ids).prefetch_related("tutorials")
        return render(request, 'tricks/add_from_list.html', {'tricks': tricks})
