dist = int(input('Digite a distancia: '))

if dist < 200:
    print('O preço da sua passagem é:R${:.2f}'.format(dist * 0.50))
else:
    print('O preço da sua passagem é:R${:.2f}'.format(dist * 0.45))
