numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero: '))
    if num > 0 and num <= 20:
        print(f'Seu numero por extenso é: {numeros[num]}')
        break
    else:
        print('Número Invalido, tente novamente.')
print('Programa finalizado')
        