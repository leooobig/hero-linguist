import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from characters.models import Personagem
from dados import DadosPersonagens


def populate():
    characters = DadosPersonagens()
    characters.filterAffiliation()
    dados = characters.listCharacters()
    for personagem in dados:
        nome, afiliacao, aliados, inimigos = personagem
        Personagem.objects.create(
            nome=nome,
            afiliacao=afiliacao,
            aliados=aliados,
            inimigos=inimigos
        )
        print(f'Adicionando personagem: {nome}')



if __name__ == '__main__':
    populate()
