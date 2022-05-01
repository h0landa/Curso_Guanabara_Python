from random import randint
from operator import itemgetter


jogo = {'jogador1': randint(1,6),
'jogador2': randint(1,6),
'jogador3': randint(1,6),
'jogador4': randint(1,6)}

ranking= {}

maior = 0
for key, valor in jogo.items():
    print(f'{key} tirou {valor} no dado ')
print('*-*-* Ranking de jogadores *-*-*')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º Lugar: Jogador {valor[0]} com {valor[1]} no dado.')
print(ranking)
    