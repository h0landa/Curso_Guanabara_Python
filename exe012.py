#Ler preço de um produto e imprimir com 5% de desconto.

preço = float(input('Qual o preço do produto?: '))

desconto = 5/100

preço_com_desconto = preço - (preço * desconto)

print('O valor do seu produto é:R${:.2f} e com desconto fica por:R${:.2f}'.format(preço,preço_com_desconto))