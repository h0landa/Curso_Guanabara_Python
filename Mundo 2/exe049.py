num = int(input('Digite um numero: '))
print(10 * '+=','TABUADA', 10 * '+=')
for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num * c))
print('Fim')
