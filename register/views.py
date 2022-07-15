from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import RegisterForm
from main.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(
                request, f'Pomyślnie zarejestrowano użytkownika {user.username}')
            return redirect(reverse('index'))

        messages.error(
            request, f'Nie udało się zarejestrować, podałeś niepoprawne dane')
        return redirect(reverse('register'))

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
