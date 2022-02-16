n1 = float(input('Digite um numero: '))

n2 = float(input('Digite um numero: '))

n3 = float(input('Digite um numero: '))

maior = 0
menor = 0

if n1 > n2 and n2 > n3:
    maior = n1
if n3 > n2 and n2 > n1:
    maior = n3
if n2 > n3 and n3 > n1:
    maior = n2
if n1 < n2 and n2 < n3:
    menor = n1
if n3 < n2 and n2 < n1:
    menor = n3
if n2 < n3 and n3 < n1:
    menor = n2

print('O maior número é:{}'.format(maior))
print('O menor número é:{}'.format(menor))
