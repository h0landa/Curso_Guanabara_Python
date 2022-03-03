num = int(input('Digite um número:'))
c = 0
soma = 0
fatorial = 1
proximo_num = 0
while c != num:
    c += 1
    fatorial = fatorial * c
    print('x'if fatorial < 1  else '='.format(c))
    print(fatorial)