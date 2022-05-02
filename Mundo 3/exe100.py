from random import randint



def sorteia(lista):
    sort = 0
    for s in range(0, 5):
        sort = randint(1, 10)
        lista.append(sort)
    print('Sorteando 5 valores da lista:', end='')
    for num in lista:
        print(num, end=' ')
    print('Pronto!')


def soma(lista):
    soma_par = 0
    for num in lista:
        if num % 2 == 0:
            soma_par += num
    print(f'Somando os valores pares de {lista}, temos {soma_par}')


sorteados = []
sorteia(sorteados)
soma(sorteados)