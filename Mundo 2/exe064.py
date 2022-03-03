exit = False
num = int(input('Digite [999] para parar: '))
c = 1
soma = 0
while num != 999:
    num = int(input('Digite [999] para parar: '))
    soma += num
    print(soma)
print('Programa encerrado')
print('A soma entre os numeros digitados é de {}'.format(soma))

    
    