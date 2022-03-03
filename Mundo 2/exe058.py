from random import randint
sorteado = randint(0,10)
acertou = False
soma = 0
while not acertou:
    num = int(input('Digite seu numero: '))
    soma = soma + 1
    if num == sorteado:
        print('Você venceu!')
        acertou = True
    else:
        if num > sorteado:
            print('Um pouco menos...')
        elif num < sorteado:
            print('Um pouco mais...')
        

print('Foram necessarias {} tentativas'.format(soma))