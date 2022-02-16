valor_casa = float(input('Digite o valor da casa: '))

salario = float(input('Digite o valor do salario: '))

quantidade_anos = int(input('Digite a quantidade de anos: ')) * 12

prestação = valor_casa/quantidade_anos

if prestação > salario * 30/100:
    print('Desculpe, não podemos fornecer um emprestimo.')
else:
    print('Emprestimo aprovado!')