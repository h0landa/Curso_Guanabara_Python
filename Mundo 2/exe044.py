preço = float(input('Digite o preço do produto: '))

print('''Escolha como que pagar pelo produto:
1 - Á vista: 10% de desconto
2 - Á vista no cartão: 5% de desconto
3 - Em até duas vezes no cartão: Preço normal
4 - Em 3x ou mais: 20% de juros''')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('Seu produto á vista fica:R${:.2f}'.format(preço - (preço * 10/100)))
elif escolha == 2:
    print('Seu produto á vista no cartão fica:R${:.2f}'.format(preço - (preço * 5/100)))
elif escolha == 3:
    print('Seu produto parcelado em até 2x fica:R${:.2f}'.format(preço))
else:
    print('Se o produto for parcelo em 3x ele fica por:R${:.2f}'.format(preço + (preço * 20/100)))
print('Tenha um bom dia!')