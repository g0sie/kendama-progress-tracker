from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tricks import views


class TestUrls(SimpleTestCase):
    def test_user_tricks_url_resolves(self):
        url = reverse('tricks:user_tricks')
        self.assertEquals(resolve(url).func, views.user_tricks)

    def test_add_new_trick_url_resolves(self):
        url = reverse('tricks:add_new_trick')
        self.assertEquals(resolve(url).func, views.add_new_trick)

    def test_add_from_list_url_resolves(self):
        url = reverse('tricks:add_from_list')
        self.assertEquals(resolve(url).func, views.add_from_list)

    def test_draw_a_trick_url_resolves(self):
        url = reverse('tricks:draw')
        self.assertEquals(resolve(url).func, views.draw_a_trick)

    def test_delete_url(self):
        url = reverse('tricks:delete', kwargs={'user_trick_id': 1})
        self.assertEquals(url, '/tricks/1/delete')
