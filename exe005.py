#Fazer um programa que leia um numero e mostre na tela seu sucessor e antecessor.
num = int(input('Digite seu numero: '))
antecessor = num - 1
sucessor = num + 1

print('O sucessor do numero {} é {}'.format(num,sucessor),
end=' \ne seu antecessor é o numero {}'.format(antecessor))