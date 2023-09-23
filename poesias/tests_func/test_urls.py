# Importando o TestCase do Django - criar testes unitários
from django.test import TestCase
# Importando o módulo necessário para trabalhar com URLs em Django
from django.urls import reverse


class URLsTest(TestCase):
    def test_ok(self):
        assert 1 == 1

    def test_fepi_url_ok(self):
        url = reverse('poesias:fepi')
        self.assertEqual(url, '/fepi')

    def test_movie_detail_url_ok(self):
        url = reverse('poesias:movie_detail', kwargs={'movie_id': 1})
        self.assertEqual(url, '/movie_detail/1/')

    def test_poema_id_url_ok(self):
        url = reverse('poesias:poema_text', kwargs={'poema_id': 2})
        self.assertEqual(url, '/poemas/2/')

# Definindo uma classe de teste que herda de TestCase.


class SearchURLTest(TestCase):

    # Esta é uma função de teste. A convenção é nomeá-la começando com "test_".
    def test_search_url_resolves(self):
        # O método 'reverse' tenta encontrar uma URL pelo seu "name".
        url = reverse('poesias:search')
        # Aqui, estamos usando uma afirmação para garantir que a URL resolvida seja '/search/'.
        # Se a URL resolvida pelo método 'reverse' for diferente de '/search/', o teste falhará.
        self.assertEqual(url, '/search/')
