from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

def make_poetry():
    return {
        'title': fake.sentence(nb_words=5),  # Títulos de poesias geralmente são curtos
        'full_text': fake.text(250),  # Texto de poesia (supondo que seja menor que uma receita)
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'genre': {  # Gênero literário da poesia
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/poetry,book' % rand_ratio(),  # Imagem relacionada a poesia ou livro
        },
        'is_popular': fake.boolean()
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_poetry())
