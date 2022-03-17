contador = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for contador in range(1, 11):
        print(f'{num} x {contador} = {num * contador}')
        contador += 1
print('Número invalido')
print('Programa encerrado')