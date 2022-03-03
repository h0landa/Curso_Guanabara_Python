num1 = float(input('Digite o 1° numero: '))
num2 = float(input('Digite o 2° numero: '))
exit = False
while not exit:
    print("=== CALCULADORA-PyCalc ===")
    print('''[1] Somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    print(27 * "=")
    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        print('A soma entre {} e {} é: {}'.format(num1, num2, num1 + num2))
    if opcao == 2:
        print('A multiplicação entre {} e {} é: {}'.format(num1, num2, num1 * num2))
    if opcao == 3:
        if num1 > num2:
            print('O primeiro número é maior que o segundo')
        else:
            print('O segundo numero é maior')
    if opcao == 4:
        num1 = float(input('Digite o 1° numero: '))
        num2 = float(input('Digite o 2° numero: ')
        )
    if opcao == 5:
        print('Programa encerrado')
        exit = True



