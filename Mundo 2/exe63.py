print(30 * '-')
print('Sequencia Fibonacci')
print(30 * '-')
quant_termos = int(input('Digite a quantidade de termos: '))
c = 3
t1 = 0
t2 = 1
print('{} --> {}'.format(t1, t2), end='')
while c <= quant_termos:
    t3 = t1 + t2
    print('--> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
    