preço = float(input('Digite o preço do produto: R$ '))

print('''Escolha como que pagar pelo produto:
1 - Á vista: 10% de desconto
2 - Á vista no cartão: 5% de desconto
3 - Em até duas vezes no cartão: Preço normal
4 - Em 3x ou mais: 20% de juros''')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    total = preço - (preço * 10/100)
elif escolha == 2:
    total = preço - (preço * 5/100)
elif escolha == 3:
    total = preço
    print('Sua compra ficou com duas parcelas de R${:.2f}'.format(preço/2))     
elif escolha == 4:
    total = preço + (preço * 20/100)
    quantparcelas = int(input('Você quer parcelar em quantas vezes ?: '))
    print('Sua compra ficará com {} parcelas de R${:.2f}'.format(quantparcelas, total/quantparcelas))
else:
    print('Opção de escolha inexistente, tente outra vez.')
print('Sua compra de R${:.2f} ficou com o valor total de R${:.2f}'.format(preço, total))
print('Tenha um bom dia!')