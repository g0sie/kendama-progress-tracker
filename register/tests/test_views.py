from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import UserProfile


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_POST_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'user123',
            'email': 'email123@op.pl',
            'password1': 'p4ssword123',
            'password2': 'p4ssword123'
        })
        user = User.objects.get(username='user123')
        userprofile = UserProfile.objects.get(user=user)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('index'))
        self.assertEquals(User.objects.all().count(), 1)
        self.assertEquals(UserProfile.objects.all().count(), 1)

    def test_register_POST_invalid(self):
        response = self.client.post(self.register_url, {
            'username': 'invaliduser123',
            'email': 'email123@op.pl',
            'password1': 'p4ssword123',
            'password2': 'p4ssword1234'
        })
        user = User.objects.filter(username='user123')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, self.register_url)
        self.assertEquals(User.objects.all().count(), 0)
        self.assertEquals(UserProfile.objects.all().count(), 0)
