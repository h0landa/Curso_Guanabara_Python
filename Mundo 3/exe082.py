main_lista = []
c = 0
while True:
    num = int(input(f'Digite o {c}ª número: '))
    if num < 0:
        break
    main_lista.append(num)
lista_pares = []
lista_impares = []
for numeros in main_lista:
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)
print(f'''Lista principal: {main_lista}
Lista de números pares:{lista_pares}
Lista de impares: {lista_impares}''')
