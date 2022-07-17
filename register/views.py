from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.contrib.auth. models import User
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from .forms import RegisterForm
from main.models import UserProfile
from .utils import token_generator


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create inactive user
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # generate link to activate
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                           'uidb64': uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://' + domain + link

            # send email
            email_subject = 'Zweryfikuj swój email'
            email_body = f'Witaj użytkowniku {user.username}! Zweryfikuj swój email klikając w link poniżej.\n' + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'twojamamakendama@gmail.com',
                [user.email],
            )
            email.send(fail_silently=False)

            messages.success(
                request, f'Zostałeś zarejestrowany użytkowniku {user.username}. Teraz potwierdź swój email!')
            return redirect(reverse('index'))

        messages.error(
            request, f'Nie udało się zarejestrować, podałeś niepoprawne dane')
        return redirect(reverse('register'))

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def email_verification(request, uidb64, token):
    # find user by uidb64
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # activate user if token is valid
    if user and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        UserProfile.objects.create(user=user)
        login(request, user)
        messages.success(
            request, f'Twoje konto zostało aktywowane użytkowniku {user.username}!')
        return redirect(reverse('index'))

    messages.error(
        request, f'Link aktywacyjny nie działa')
    return redirect(reverse('index'))
