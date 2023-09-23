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

    def test_search_view_returns_search_template(self):
        # Utiliza o cliente de teste para fazer uma requisição
        # GET para a URL nomeada 'search'.
        response = self.client.get(reverse('poesias:search'))

        # Verifica se a resposta utiliza o template esperado 'search.html'.
        self.assertTemplateUsed(response, 'search.html')
