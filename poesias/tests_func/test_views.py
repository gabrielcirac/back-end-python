from django.test import TestCase
from django.urls import reverse, resolve
from poesias import views


class ViewsTests(TestCase):
    def test_home_view_is_correct(self):
        view = resolve(reverse('poesias:home'))
        self.assertIs(view.func, views.home)

    def test_movie_detail_view_is_correct(self):
        view = resolve(reverse(
            'poesias:movie_detail', kwargs={'movie_id': 1}))
        self.assertIs(view.func, views.movie_detail)

    def test_poema_id_view_is_correct(self):
        view = resolve(
            reverse('poesias:poema_text', kwargs={'poema_id': 2}))
        self.assertIs(view.func, views.poema_text)
