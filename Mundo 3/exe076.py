listagem_precos = ('Cadeira Gamer - Pichau', 570, 'Mouse Gamer - Razer', 200,
                   'Teclado Gamer - RedDragon', 250, 'Gabinete - Pichau', 400, 'Monitor - AOC', 1700)
print('---------- TABELA DE PREÇOS ----------')
for produtos in range(0, 10):
    if produtos % 2 == 0:
        print(f'{listagem_precos[produtos]:.<30}', end='')
    else:
        print(f'R${listagem_precos[produtos]:.2f}')
print(39 * '-')
