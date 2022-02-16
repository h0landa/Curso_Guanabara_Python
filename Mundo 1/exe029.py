velocidade = int(input('Digite sua velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Sua velocidade está acima de 80Km/h')
    print('Você precisa pagar uma multa no valor de:R${}'.format(multa))
else:
    print('Você não possui multas')

