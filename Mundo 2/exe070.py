opção = ''
total_gasto = 0
mais_de_1000 = 0
mais_barato = 0
nome_produto_mais_barato = ''
while opção != 'N':
    nome_produto = str(input('Digite o nome do produto: ')).upper()
    valor_produto = float(input('Digite o valor do produto: '))
    opção = str(input('Quer continuar[S/N]: ')).upper()
    total_gasto += valor_produto
    mais_barato = valor_produto
    nome_produto_mais_barato = nome_produto
    if valor_produto < mais_barato:
        mais_barato = valor_produto
        nome_produto_mais_barato = nome_produto
    if valor_produto > 1000:
        mais_de_1000 += 1
print(f'Total gasto:{total_gasto}')
print(f'Mais barato:{nome_produto_mais_barato}')
print(f'Produtos acima de R$1000:{mais_de_1000}')
