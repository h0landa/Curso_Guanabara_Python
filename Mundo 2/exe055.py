for c in range(1,6):
    peso = float(input('Digite peso {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg'.format(maior, menor))
