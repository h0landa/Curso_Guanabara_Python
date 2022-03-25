n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = (n1, n2, n3, n4)
quant_nove = quant_pares = 0
for num in range(0, 4):
    if tupla[num] == 9:
        quant_nove += 1
    if tupla[num] % 2 == 0:
        quant_pares += 1
    if 3 in tupla:
        resultado = f'O número 3 aparece na lista na posição -> {tupla.index(3)}'
    if 3 not in tupla:
        resultado = 'O número 3 não aparece na tupla'
print(f'''Números na tupla:{tupla}
Quantidade de pares:{quant_pares}
Vezes que o 9 aparece:{quant_nove}''')
print(f'Posição em que aparece o 3:{resultado}')
