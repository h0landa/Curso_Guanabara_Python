from random import choice, choices
numeros = []
for c in range(0, 20):
    numeros.append(c)
sorteio = choices(numeros, k=5)
maior_num = sorteio[0]
menor_num = sorteio[0]
for c in range(0, 5):
    if sorteio[c] > maior_num:
        maior_num = sorteio[c]
    if sorteio[c] < menor_num:
        menor_num = sorteio[c]
print(f'''Números sorteados:{sorteio}
Maior número sorteado:{maior_num}
Menor número sorteado:{menor_num}''')
