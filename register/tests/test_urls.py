from django.test import SimpleTestCase
from django.urls import reverse, resolve

from register.views import register


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
