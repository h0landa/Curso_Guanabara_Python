from random import choice
contador = 0
while True:
    jogador = str(input('Digite sua escolha: ')).strip().upper()
    alternativas = ['Par','Impar']
    computador = choice(alternativas).upper()
    if jogador == computador:
        contador += 1
    if jogador != computador:
        break
print('Você foi derrotado')
print(f'Vitorias consecutivas:{contador}')
    
    