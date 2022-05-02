import random


print(35 * '#')
print('          MEGA SENA')
print(35 * '#')
quant_jogos = int(input('Quantos jogos você quer sortear ?: '))
palpites = []
print(f'*-*-*-* SORTEANDO {quant_jogos} JOGOS *-*-*-*')
for jogos in range(0, quant_jogos):
    palpites = []
    for cont in range(0, 6):
        sorteado = random.randint(1, 100)
        palpites.append(sorteado)
    print(f'Jogo {jogos + 1}: {palpites}')
print('BOA SORTE...')