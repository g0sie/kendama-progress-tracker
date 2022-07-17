from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import RegisterForm
from main.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            email = EmailMessage(
                'Potwierdź swój email',
                f'Witaj użytkowniku {user.username}! Potwierdź swój email klikając w link poniżej.',
                f'twojamamakendama@gmail.com',
                [user.email],
            )
            email.send(fail_silently=False)

            UserProfile.objects.create(user=user)
            messages.success(
                request, f'Zostałeś zarejestrowany użytkowniku {user.username}. Teraz potwierdź swój email!')
            return redirect(reverse('index'))

        messages.error(
            request, f'Nie udało się zarejestrować, podałeś niepoprawne dane')
        return redirect(reverse('register'))

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
