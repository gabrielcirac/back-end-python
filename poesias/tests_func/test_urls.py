from django.test import TestCase
from django.urls import reverse


class UTLsTest(TestCase):
    def test_ok(self):
        assert 1 == 1

    def test_home_url_ok(self):
        home_url = reverse('poesias:home')
        self.assertEqual(home_url, '/')
