from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tutorials.views import add_tutorials


class TestUrls(SimpleTestCase):
    def test_add_url_resolves(self):
        url = reverse('tutorials:add', kwargs={'number': 1})
        self.assertEquals(resolve(url).func, add_tutorials)
