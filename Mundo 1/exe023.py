# O programa deve ler um numero de 0 a 9999 e mostrar na tela cada digito separado.

num = str(input('Digite um numero: '))
n = int(num)

u = n // 1 % 10

d = n // 10 % 10

c = n // 100 % 10

m = n // 1000 % 10

print('Para o numero {} temos: \n Unidade:{} \n Dezena:{} \n Centena:{} \n Milhar:{}'.format(n, u, d, c, m))