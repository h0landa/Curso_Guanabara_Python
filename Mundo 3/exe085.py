lista_suprema = []
impar = []
par = []
for c in range(0, 7):
    num = int(input(f'Digite o {c}ª valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista_suprema.append(par)
lista_suprema.append(impar)
print(f'''Esses são os números impares:{sorted(lista_suprema[1])}
Esses são os números pares: {sorted(lista_suprema[0])}''')