from random import choice

l = [1,2,3,4,5]

num = int(input('Digite um numero: '))

sorteado = choice(l)

if num == sorteado:
    print('Você venceu!')
else:
    print('Numero certo:{}'.format(sorteado))
    print('Computer Winsssss')
    print('*** GAME OVER ***')


