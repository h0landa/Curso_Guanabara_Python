r1 = int(input('Digite a primeira reta: '))

r2 = int(input('Digite a segunda reta: '))

r3 = int(input('Digite a terceira reta: '))

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('Essas retas não formam um triângulo')
else:
    print('Formam um triângulo')

