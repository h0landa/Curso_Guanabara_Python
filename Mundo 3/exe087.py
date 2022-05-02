matriz = [[], [], []]
soma_pares = soma_terceira_col = 0
linhas = 0
for coluna in matriz:
    for campos in range(0, 3):
        num = int(input(f'Digite um número para[{linhas, campos}]: '))
        if num % 2 == 0:
            soma_pares += num
        coluna.append(num)
    linhas += 1
print(35 * '#')
for registros in matriz:
    contador = 0
    print(f'[  {registros[contador]}  ] [  {registros[contador + 1]}  ] [  {registros[contador + 2]}  ]')
    contador += 3 
print(35 * '#')
print(f'''Soma dos pares: {soma_pares}
Soma dos valores da terceira coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}
Maior valor da segunda linha: {max(matriz[1])}''')
