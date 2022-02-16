#Ler quanto dinheiro tem em uma carteira e mostrar quantos dolares ela pode comprar
dolar = 3.27
carteira = float(input('Digite quantos reais você tem na carteira: '))

resultado = carteira/dolar

print('Com {} reais você pode comprar um total de:{:.2f} dólares!'.format(carteira,resultado))