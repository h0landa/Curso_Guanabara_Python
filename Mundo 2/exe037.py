num = int(input('Digite um número inteiro: '))
print('''Escolha as opcções de conversão:
1 - BINARIO
2 - HEXADECIMAL
3 - OCTAL''')
opçao = int(input('Digite a opção:'))
if opçao == 1:
    print('O número {} convertido para binario é:{}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} convertido para hexadecimal é:{}'.format(num, hex(num)[2:]))
elif opçao == 3:
    print('O número {} convertido para octal é:{}'.format(num, oct(num)[2:]))
else:
    print('A opção {} não existe'.format(opçao))