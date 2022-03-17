soma = contador = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A quantidade de números digitados foi de {contador} e a soma entre eles foi de {soma}')
    