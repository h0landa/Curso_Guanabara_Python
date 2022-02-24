num = int(input('Digite um numero: '))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        contador += 1
        print(c)
print('O numero {} foi divisivel {} vezes'.format(num, contador))
if contador > 2:
    print('E por isso ele não é primo')
else:
    print('E por isso ele é primo')