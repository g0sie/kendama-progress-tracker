from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm
from main.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
        else:
            return redirect(reverse('register'))
        return redirect(reverse('index'))

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
