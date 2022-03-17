num = int(input('Digite [999] para parar: '))
c = 0
soma = num
while num != 999:
    num = int(input('Digite [999] para parar: '))
    soma += num
print('Programa encerrado')
print('A soma entre os numeros digitados é de {}'.format(soma - 999))

    
    