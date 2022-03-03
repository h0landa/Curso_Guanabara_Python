c = maior_num = menor_num = soma = 0
continuacao = 'S'
while continuacao != 'N':
    num = int(input('Digite um numero: '))
    soma += num
    c += 1
    if c == 1:
        maior_num = num
    elif num < maior_num:
        menor_num = num
    elif num > maior_num:
        maior_num = num
    continuacao = str(input('Quer continuar [S/N]: ')).strip().upper()
media = soma/c
print('Você digitou {} números e a média entre eles foi de {}'.format(c, media))
print('O maior número foi {} e o menor foi {}'.format(maior_num, menor_num))