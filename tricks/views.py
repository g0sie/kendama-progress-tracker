import random

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Case, When, Value

from .models import Trick, UserTrick
from .forms import TrickForm


@login_required
def user_tricks(request):
    """displays list of a user's tricks"""
    if request.method == 'POST':
        # if user clicked '+1' button
        land_keys = [key for key in request.POST.keys()
                     if key.startswith("land_")]
        if land_keys:
            key = int(land_keys[0].split("_")[1])
            land_trick(key)
        # if user clicked 'rank up' button
        rank_up_keys = [key for key in request.POST.keys()
                        if key.startswith("rankup_")]
        if rank_up_keys:
            key = int(rank_up_keys[0].split("_")[1])
            rank_up_trick(key)
        return HttpResponseRedirect(reverse('tricks:user_tricks'))

    tricks_number = request.GET.get('tricks', 12)
    user_trick_pairs = UserTrick.objects.filter(user=request.user) \
        .select_related("trick").prefetch_related("trick__tutorials") \
        .order_by(
            "rank",
            Case(
                When(trick__difficulty='b', then=Value(0)),
                When(trick__difficulty='i', then=Value(1)),
                When(trick__difficulty='a', then=Value(2)),
                default=Value(3)
            ),
            "-trick__official"
    )

    paginator = Paginator(user_trick_pairs, tricks_number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tricks/user_tricks.html", {'user_trick_pairs': page_obj, 'tricks_number': tricks_number})


def land_trick(user_trick_id: int):
    user_trick = UserTrick.objects.get(id=user_trick_id)
    if user_trick.land_count <= 100:
        user_trick.land_count += 1
        user_trick.save()


def rank_up_trick(user_trick_id: int):
    """if the requirements are met the trick ranks up and user gets 10 kens"""
    requirements = {
        1: 10,
        2: 25,
        3: 50,
        4: 100,
        5: 999,
    }
    user_trick = UserTrick.objects.get(id=user_trick_id)
    if user_trick.land_count >= requirements[user_trick.rank]:
        user_trick.user.profile.kens += 10
        user_trick.user.profile.save()
        user_trick.rank += 1
        user_trick.save()


@login_required
def add_new_trick(request):
    if request.method == "POST":
        form = TrickForm(data=request.POST)
        if form.is_valid():
            trick = form.save()
            UserTrick.objects.create(user=request.user, trick=trick)
            HttpResponseRedirect(reverse("tricks:add_new_trick"))
    form = TrickForm()
    return render(request, 'tricks/add_new_trick.html', {'form': form})


@login_required
def add_from_list(request):
    """displays official trick list"""
    if request.method == "POST":
        # get id of the trick to add
        add_keys = [key for key in request.POST.keys()
                    if key.startswith("add_")]
        add_key = int(add_keys[0].split("_")[1])
        # check if user has the trick already
        if add_key not in UserTrick.objects.filter(user=request.user).values_list("trick__id", flat=True):
            trick = Trick.objects.get(id=add_key)
            UserTrick.objects.create(user=request.user, trick=trick)

    tricks_number = request.GET.get('tricks', 8)
    # display only the tricks the user doesn't have
    user_tricks_ids = UserTrick.objects.filter(
        user=request.user).values('trick__id')
    tricks = Trick.objects.filter(official=True).exclude(
        id__in=user_tricks_ids).order_by(
            Case(
                When(difficulty='b', then=Value(0)),
                When(difficulty='i', then=Value(1)),
                When(difficulty='a', then=Value(2)),
                default=Value(3)
            )
    ).prefetch_related("tutorials")

    paginator = Paginator(tricks, tricks_number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tricks/add_from_list.html', {'tricks': page_obj, 'tricks_number': tricks_number})


def get_random_user_trick(user):
    user_tricks = UserTrick.objects.filter(user=user, rank__lte=5)
    count = user_tricks.count()
    if count > 0:
        return user_tricks[random.randint(0, count - 1)]
    return None


@login_required
def draw_a_trick(request):
    if request.method == 'POST':
        # if user clicked 'land' button
        land_keys = [key for key in request.POST.keys()
                     if key.startswith("land_")]
        if land_keys:
            key = int(land_keys[0].split("_")[1])
            land_trick(key)
            request.user.profile.kens += 1
            request.user.profile.save()
        return HttpResponseRedirect(reverse('tricks:draw'))

    # get random user trick
    user_trick = get_random_user_trick(request.user)
    if user_trick:
        return render(request, 'tricks/draw_a_trick.html', {'user_trick': user_trick})
    return render(request, 'tricks/draw_a_trick_but_no_trick.html')
