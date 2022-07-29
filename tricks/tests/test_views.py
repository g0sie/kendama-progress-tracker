from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='user123')
        self.user.set_password('p4ssword123')
        self.user.save()
        self.user_tricks_url = reverse('tricks:user_tricks')

    def test_user_tricks_GET_not_logged_in(self):
        response = self.client.get(self.user_tricks_url)

        self.assertEquals(response.status_code, 302)
        self.assertIn(settings.LOGIN_URL, response.url)

    def test_user_tricks_GET_logged_in(self):
        logged_in = self.client.login(
            username='user123', password='p4ssword123')
        response = self.client.get(self.user_tricks_url)

        self.assertTrue(logged_in)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tricks/user_tricks.html')

    def test_user_tricks_POST_not_logged_in(self):
        response = self.client.get(self.user_tricks_url)

        self.assertEquals(response.status_code, 302)
        self.assertIn(settings.LOGIN_URL, response.url)

    def test_user_tricks_POST_logged_in(self):
        self.client.login(username='user123', password='p4ssword123')
        response = self.client.post(self.user_tricks_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, self.user_tricks_url)
