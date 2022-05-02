matriz = [[],[],[]]
for count in range(0, 3):
    for c in range(0 ,3):
        num = int(input(f'Digite um valor para[{count},{c}]:'))
        matriz[count].append(num)
for registros in matriz:
    contador = 0
    print(f'[  {registros[contador]}  ] [  {registros[contador + 1]}  ] [  {registros[contador + 2]}  ]')
    contador += 3    
print(matriz)
