from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tricks.views import user_tricks, add_new_trick, add_from_list, draw_a_trick


class TestUrls(SimpleTestCase):
    def test_user_tricks_url_resolves(self):
        url = reverse('tricks:user_tricks')
        self.assertEquals(resolve(url).func, user_tricks)

    def test_add_new_trick_url_resolves(self):
        url = reverse('tricks:add_new_trick')
        self.assertEquals(resolve(url).func, add_new_trick)

    def test_add_from_list_url_resolves(self):
        url = reverse('tricks:add_from_list')
        self.assertEquals(resolve(url).func, add_from_list)

    def test_draw_a_trick_url_resolves(self):
        url = reverse('tricks:draw')
        self.assertEquals(resolve(url).func, draw_a_trick)
